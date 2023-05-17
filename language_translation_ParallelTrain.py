import argparse, sys, copy, os
from transformers import RobertaTokenizer, T5ForConditionalGeneration, AutoTokenizer
from evaluation.compute_compilationErr_strtEnd import computeErrMetric_forPredFile
from timeit import default_timer as timer
import pandas as pd
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from torch import Tensor
import torch
import torch.nn as nn
from torch.nn import Transformer
import math
import numpy as np
import random
import LT_utils_CFLoss
import wandb
from accelerate import Accelerator
import subprocess, shutil
import re, time
from itertools import islice
import pytorch_lightning as pl
from torchmetrics import Metric
import cProfile, pstats, io
from os import listdir
from os.path import isfile, join

#os.environ["WANDB_START_METHOD"] = "thread"
    
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def modifiedPrint(*stringsToPrint):
    for arg in stringsToPrint:
        print (arg, end=" ", flush=True)
    print ("", flush=True)

def argParse_helperFunc():
    #=================== SETTING ARGPARSE ARGUMENTS ====================
    parser = argparse.ArgumentParser()
    parser.add_argument('--cf_mode', type=int, required=False, default="0")
    parser.add_argument('--cf_weight', type=float, required=False, default="0.5") #BETWEEN 0 AND 1
    parser.add_argument('--model_name', type=str, required=False, default="NA")
    parser.add_argument('--model_tag', type=str, required=False, default="NA")
    parser.add_argument('--model_notes', type=str, required=False, default="NA")
    parser.add_argument('--src_lang', type=str, required=True, choices=["java", "python"])
    parser.add_argument('--dest_lang', type=str, required=True, choices=["java", "python"])
    parser.add_argument('--num_epochs', type=int, required=False, default=200)
    parser.add_argument('--num_nodes', type=int, required=True, default=1)
    parser.add_argument('--num_gpus_per_node', type=int, required=True, default=1)
    parser.add_argument('--num_cpu_workers', type=int, required=True, default=1)
    parser.add_argument('--batch_size', type=int, required=True, default=8)
    parser.add_argument('--writeDir', type=str, required=True)
    args = parser.parse_args()
    if (not args.cf_mode): 
        args.cf_weight = 0
    assert (args.cf_weight <= 1) and (args.cf_weight >= 0)
    modifiedPrint(args)
    return args

#==================== SETTING UP CUSTOM DATASET ====================
class CustomDataset(Dataset):
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def __getitem__(self, index):
        input_ids_src = self.dataframe.loc[index, "input_ids_src"]
        input_ids_tgt = self.dataframe.loc[index, "input_ids_tgt"]
        probID = self.dataframe.loc[index, "probID"]
        return input_ids_src, input_ids_tgt, probID

    def __len__(self):
        return len(self.dataframe)

#================== CUSTOM METRIC ======================
class CodeQualityMetrics(Metric):
    def __init__(self, transformerTokenizer, writeDir, DEST_LANG):
        super().__init__()
        self.transformerTokenizer = transformerTokenizer
        self.writeDir = writeDir
        self.DEST_LANG = DEST_LANG
        self.add_state("totalSamples", default = torch.tensor(0, dtype = torch.int), dist_reduce_fx = "sum")
        self.add_state("allPredList", default = [], dist_reduce_fx = None)
        self.add_state("allTargList", default = [], dist_reduce_fx = None)
        self.add_state("allIDList", default = [], dist_reduce_fx = None)
        self.add_state("loss_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("compilation_succ_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("runtimeEqCount_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("bleu_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("exact_match_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("ngram_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("weighted_ngram_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("syntax_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("dataflow_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("codebleu_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")
        self.add_state("errStrtMetric_sum", default = torch.tensor(0, dtype = torch.float), dist_reduce_fx = "sum")

    def _calcMetrics(self, pathPrediction, pathReference, pathID, writeDirTmp):
        # calculate errStrtMetric
        errStrtMetric = computeErrMetric_forPredFile(pathPrediction, 
                                        self.DEST_LANG, writeDirTmp) #-------CHECK WRITE PATH, GPU SPECIFIC

        # evaluate, checking compiling rate
        command1 = ["python", "./AVATAR_data/evaluation/compile.py", 
                    "--input_file", pathPrediction, 
                    "--language", self.DEST_LANG,
                    "--writeDir", writeDirTmp]

        # evaluate, checking BLEU score
        command2 = ["python", "./AVATAR_data/evaluation/evaluator.py", 
                    "--references", pathReference,
                    "--txt_ref",
                    "--predictions", pathPrediction, 
                    "--language", self.DEST_LANG]

        # evaluate, checking CodeBLEU score
        command3 = ["python", "./AVATAR_data/evaluation/CodeBLEU/calc_code_bleu.py", 
                    "--ref", pathReference,
                    "--txt_ref",
                    "--hyp", pathPrediction, 
                    "--lang", self.DEST_LANG]

        # evaluate, checking runtime equivalence score
        command4 = ["python", "./AVATAR_data/data_LARGE/runtimeEquivalence_corrections/check_runtimeOutput.py", 
                    "--input_file", pathPrediction,
                    "--id_file", pathID,
                    "--language", self.DEST_LANG,
                    "--writeDir", writeDirTmp]
                    
        #print ("\n\n\n\nXXXXX\n\n\n", " ".join(command4))

        allCommands = "; ".join([" ".join(command1), " ".join(command2), " ".join(command3), 
                        " ".join(command4)])
        p = subprocess.run(allCommands, capture_output = True, shell = True)
        all_stdout = p.stdout.decode()

        #print ("\n\n", all_stdout, "\n\n")

        compilation_succ, bleu, exact_match, ngram, weighted_ngram, \
                    syntax, dataflow, codebleu, runtimeEqCount = -1,-1,-1,-1,-1,-1,-1,-1,-1

        match = re.search('Success - (\d+)', all_stdout)
        if match: compilation_succ = int(match.group(1))

        match = re.search('BLEU:\s*(\d+\.\d+)', all_stdout)
        if match: bleu = float(match.group(1))

        match = re.search('Exact Match:\s*(\d+\.\d+)', all_stdout)
        if match:  exact_match = float(match.group(1))

        match = re.search('Ngram match:\s*(\d+\.\d+)', all_stdout)
        if match: ngram = float(match.group(1))

        match = re.search('Weighted ngram:\s*(\d+\.\d+)', all_stdout)
        if match: weighted_ngram = float(match.group(1))

        match = re.search('Syntax match:\s*(\d+\.\d+)', all_stdout)
        if match: syntax = float(match.group(1))

        match = re.search('Dataflow match:\s*(\d+\.\d+)', all_stdout)
        if match: dataflow = float(match.group(1))

        match = re.search('CodeBLEU score:\s*(\d+\.\d+)', all_stdout)
        if match: codebleu = float(match.group(1))

        match = re.search('Success-RuntimeEq - (\d+)', all_stdout)
        if match: runtimeEqCount = float(match.group(1))
        
        return {"compilation_succ": compilation_succ, 
                "bleu": bleu, 
                "exact_match": exact_match, 
                "ngram": ngram, 
                "weighted_ngram": weighted_ngram,
                "syntax": syntax, 
                "dataflow": dataflow,
                "codebleu": codebleu,
                "errStrtMetric": errStrtMetric,
                "runtimeEqCount": runtimeEqCount}

    def savePredictions(pred_oneLineCodeList, target_oneLineCodeList, probIDs, tempFolderNm, suffixStr = None):
        if suffixStr is not None:
            suffixStr = "_" + suffixStr
        else:
            suffixStr = ""
        savePathPred = os.path.join(tempFolderNm, 'PRED{}.txt'.format(suffixStr))
        savePathTarget = os.path.join(tempFolderNm, 'TARG{}.txt'.format(suffixStr))
        savePathID = os.path.join(tempFolderNm, 'ID{}.txt'.format(suffixStr))

        #assert not os.path.exists(savePathPred)
        with open(savePathPred, 'w') as f:
            for i in range(len(pred_oneLineCodeList)):
                if i != len(pred_oneLineCodeList) - 1:
                    f.write(pred_oneLineCodeList[i])
                    f.write('\n')
                else:
                    f.write(pred_oneLineCodeList[i])

        #assert not os.path.exists(savePathTarget)
        with open(savePathTarget, 'w') as f:
            for i in range(len(target_oneLineCodeList)):
                if i != len(target_oneLineCodeList) - 1:
                    f.write(target_oneLineCodeList[i])
                    f.write('\n')
                else:
                    f.write(target_oneLineCodeList[i])

        if probIDs is not None:
            with open(savePathID, 'w') as f:
                for i in range(len(probIDs)):
                    if i != len(probIDs) - 1:
                        f.write(probIDs[i])
                        f.write('\n')
                    else:
                        f.write(probIDs[i])

        return savePathPred, savePathTarget, savePathID

    def _removePredictions(self, predPath, targetPath, IDPath):
        assert os.path.exists(predPath)
        os.remove(predPath)        
        assert os.path.exists(targetPath)          
        os.remove(targetPath)
        assert os.path.exists(IDPath)          
        os.remove(IDPath)
        return True

    def update(self, preds: torch.Tensor, loss: float, target: torch.Tensor, probIDs,
                    batch_idx: int, epochNum: int, device_id: str):

        predIDList = [preds[i,:] for i in range (preds.size()[0])]
        targIDList = [target[i,:] for i in range (target.size()[0])]
        self.allPredList.extend(predIDList)
        self.allTargList.extend(targIDList)
        self.allIDList.extend(probIDs)

        time_rand_str = "metricCalc_" + str(int(round(time.time() * 1000))) + "_" + \
                                str(random.randint(1000,9999)) + \
                                "_batch{}_epoch{}_device{}".format(
                                            batch_idx, epochNum, device_id)
        tempFolderNm = os.path.join(self.writeDir, time_rand_str)
        os.makedirs(tempFolderNm, exist_ok = False)

        #print ("\n\n\n\n\n\nZZZZZZ\n\n\n", self.writeDir, time_rand_str, tempFolderNm)

        assert preds.shape == target.shape #batch_size * 512

        decodedPredList = self.transformerTokenizer.batch_decode(predIDList, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False)
        decodedTargetList = self.transformerTokenizer.batch_decode(targIDList, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False)

        #print ("\n\n\n\n\n\nYYYYYYY\n\n\n", probIDs)

        savePathPred, savePathTarget, savePathID = CodeQualityMetrics.savePredictions(decodedPredList, 
                                            decodedTargetList, 
                                            probIDs, tempFolderNm)

        mets = self._calcMetrics(savePathPred, savePathTarget, savePathID, tempFolderNm)
        self._removePredictions(savePathPred, savePathTarget, savePathID) 

        numSamplesInBatch = target.size(dim = 0)
        self.totalSamples +=  numSamplesInBatch

        self.compilation_succ_sum += mets["compilation_succ"] #NOTE: no mult by numSamplesInBatch here (bcos count)
        self.bleu_sum += mets["bleu"] * numSamplesInBatch
        self.exact_match_sum += mets["exact_match"] * numSamplesInBatch
        self.ngram_sum += mets["ngram"] * numSamplesInBatch
        self.weighted_ngram_sum += mets["weighted_ngram"] * numSamplesInBatch
        self.syntax_sum += mets["syntax"] * numSamplesInBatch
        self.dataflow_sum += mets["dataflow"] * numSamplesInBatch
        self.codebleu_sum += mets["codebleu"] * numSamplesInBatch
        self.errStrtMetric_sum += mets["errStrtMetric"] * numSamplesInBatch
        self.runtimeEqCount_sum += mets["runtimeEqCount"] #NOTE: no mult by numSamplesInBatch here
        self.loss_sum += loss * numSamplesInBatch

        assert os.path.exists(tempFolderNm)
        shutil.rmtree(tempFolderNm) 

    def compute(self, dataPartition = "", epochNum = "INIT", deviceID = "gpu"):
        metsOverall = {}
        metsOverall["{}_numSamples".format(dataPartition)] = self.totalSamples.detach().cpu()
        metsOverall["{}_compilation_succ".format(dataPartition)] = self.compilation_succ_sum.detach().cpu()
        metsOverall["{}_runtimeEquiv_succ".format(dataPartition)] = self.runtimeEqCount_sum.detach().cpu()
        metsOverall["{}_bleu".format(dataPartition)] = (self.bleu_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_exact_match".format(dataPartition)] = (self.exact_match_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_ngram_match".format(dataPartition)] = (self.ngram_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_weighted_ngram".format(dataPartition)] = (self.weighted_ngram_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_syntax_match".format(dataPartition)] = (self.syntax_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_dataflow_match".format(dataPartition)] = (self.dataflow_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_codebleu".format(dataPartition)] = (self.codebleu_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_mean_errStrtByProgLen".format(dataPartition)] = (self.errStrtMetric_sum.float() / self.totalSamples).detach().cpu()
        metsOverall["{}_loss".format(dataPartition)] = (self.loss_sum.float() / self.totalSamples).detach().cpu()

        epochPath = os.path.join(self.writeDir, "epoch_{}".format(epochNum))
        os.makedirs(epochPath, exist_ok=True)

        allDecodedPredList = self.transformerTokenizer.batch_decode(torch.stack(self.allPredList), 
                                                                    skip_special_tokens = True,
                                                                    clean_up_tokenization_spaces = False)
        allDecodedTargList = self.transformerTokenizer.batch_decode(torch.stack(self.allTargList), 
                                                                    skip_special_tokens = True,
                                                                    clean_up_tokenization_spaces = False)

        savePathPred, savePathTarget, savePathID = CodeQualityMetrics.savePredictions(allDecodedPredList, allDecodedTargList, 
                                        None, epochPath,  
                                        "{}_epoch{}_{}".format(dataPartition, epochNum, deviceID))
        
        return metsOverall

#==================== TOKENIZE DATA & DATALOADER STUFFS ====================
class CodeTranslationDataModule(pl.LightningDataModule):
    def __init__(self, src_lang, dest_lang, tokenizer, pathDict, writeDir, DEBUG_FLAG,
                    train_batch_size, eval_batch_size, num_cpu_workers):
        super().__init__()
        self.src_lang = src_lang
        self.dest_lang = dest_lang
        self.tokenizer = tokenizer
        self.pathDict = pathDict
        self.writeDir = writeDir
        self.DEBUG_FLAG = DEBUG_FLAG
        self.train_bs = train_batch_size
        self.eval_bs = eval_batch_size
        self.num_cpu_workers = num_cpu_workers

        self.train_data = None
        self.val_data = None
        self.test_data = None
        self.testRefPath = self.writeDir + '/{}_testReferences.txt'.format(self.dest_lang)
        self.valRefPath = self.writeDir + '/{}_valReferences.txt'.format(self.dest_lang)

    def prepare_data(self):
        #------------------ SETTING DATA PATHS ------------------
        if (self.src_lang == 'java') and (self.dest_lang == 'python'):
            TxDirectionKey = 'java2py'
        elif (self.src_lang == 'python') and (self.dest_lang == 'java'):
            TxDirectionKey = 'py2java'
        else:
            sys.exit(0)
        if self.DEBUG_FLAG:
            TxDirectionKey += "_debug"

        path_AVATAR_training_data_source = self.pathDict[TxDirectionKey]['train_source']
        path_AVATAR_training_data_reference = self.pathDict[TxDirectionKey]['train_ref']
        path_AVATAR_training_data_id = self.pathDict[TxDirectionKey]['train_id']
        path_AVATAR_validate_data_source = self.pathDict[TxDirectionKey]['val_source']
        path_AVATAR_validate_data_reference = self.pathDict[TxDirectionKey]['val_ref']
        path_AVATAR_validate_data_id = self.pathDict[TxDirectionKey]['val_id']
        path_AVATAR_test_data_source = self.pathDict[TxDirectionKey]['test_source']
        path_AVATAR_test_data_reference = self.pathDict[TxDirectionKey]['test_ref']
        path_AVATAR_test_data_id = self.pathDict[TxDirectionKey]['test_id']

        path_valReference = self.valRefPath
        path_testReference = self.testRefPath

        shutil.copy(path_AVATAR_validate_data_reference, path_valReference) #overwrites if already present
        shutil.copy(path_AVATAR_test_data_reference, path_testReference) #overwrites if already present

        #------------------ READING DATA ------------------
        src_training_data = []
        dest_training_data = []
        src_validate_data = []
        dest_validate_data = []
        ids_validate = []
        src_test_data = []
        dest_test_data = []
        ids_test = []

        modifiedPrint("Started reading dataset...\n")

        with open(path_AVATAR_training_data_source, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                src_training_data.append(line.strip().replace("\t", "    "))
            f.close()

        with open(path_AVATAR_training_data_reference, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                dest_training_data.append(line.strip().replace("\t", "    "))
            f.close()

        assert len(src_training_data) == len(dest_training_data)
        training_dataset = list(zip(src_training_data, dest_training_data))

        with open(path_AVATAR_validate_data_source, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                src_validate_data.append(line.strip().replace("\t", "    "))
            f.close()

        with open(path_AVATAR_validate_data_reference, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                dest_validate_data.append(line.strip().replace("\t", "    "))
            f.close()

        with open(path_AVATAR_validate_data_id, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                ids_validate.append(line.strip().replace("\t", "    "))
            f.close()

        assert len(src_validate_data) == len(dest_validate_data)
        assert len(dest_validate_data) == len(ids_validate)
        validate_dataset = list(zip(src_validate_data, dest_validate_data, ids_validate))

        with open(path_AVATAR_test_data_source, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                src_test_data.append(line.strip().replace("\t", "    "))
            f.close()

        with open(path_AVATAR_test_data_reference, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                dest_test_data.append(line.strip().replace("\t", "    "))
            f.close()

        with open(path_AVATAR_test_data_id, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                ids_test.append(line.strip().replace("\t", "    "))
            f.close()

        assert len(src_test_data) == len(dest_test_data)
        assert len(dest_test_data) == len(ids_test)
        test_dataset = list(zip(src_test_data, dest_test_data, ids_test))

        modifiedPrint ("\n-----------------------")
        modifiedPrint("    Dataset Details:    ")
        modifiedPrint("-----------------------")
        modifiedPrint("# of Training samples:", len(training_dataset))
        modifiedPrint("# of Validation samples:", len(validate_dataset))
        modifiedPrint("# of Test samples:", len(test_dataset))
        modifiedPrint("-----------------------\n")

        tokenized_train = [(LT_utils_CFLoss.tokenize_code(sample[0], self.tokenizer).flatten(),
                            LT_utils_CFLoss.tokenize_code(sample[1], self.tokenizer).flatten(),
                            0) for #NOTE: put 0 here, to reduce memory
                        sample in training_dataset]
        tokenized_val = [(LT_utils_CFLoss.tokenize_code(sample[0], self.tokenizer).flatten(),
                            LT_utils_CFLoss.tokenize_code(sample[1], self.tokenizer).flatten(),
                            sample[2]) for
                        sample in validate_dataset]
        tokenized_test = [(LT_utils_CFLoss.tokenize_code(sample[0], self.tokenizer).flatten(),
                            LT_utils_CFLoss.tokenize_code(sample[1], self.tokenizer).flatten(),
                            sample[2]) for
                        sample in test_dataset]

        df_tokenized_train = pd.DataFrame(tokenized_train, columns=["input_ids_src", "input_ids_tgt", "probID"])
        df_tokenized_val = pd.DataFrame(tokenized_val, columns=["input_ids_src", "input_ids_tgt", "probID"])
        df_tokenized_test = pd.DataFrame(tokenized_test, columns=["input_ids_src", "input_ids_tgt", "probID"])

        modifiedPrint("\n----- Train DataFrame -----\n")
        modifiedPrint(df_tokenized_train.iloc[0]["input_ids_src"].shape)
        modifiedPrint(df_tokenized_train)

        modifiedPrint("\n----- Valid DataFrame -----\n")
        modifiedPrint(df_tokenized_val.iloc[0]["input_ids_src"].shape)
        modifiedPrint(df_tokenized_val)

        modifiedPrint("\n----- Test DataFrame -----\n")
        modifiedPrint(df_tokenized_test.iloc[0]["input_ids_src"].shape)
        modifiedPrint(df_tokenized_test)

        df_tokenized_train.to_pickle(os.path.join(self.writeDir, "df_tokenized_train.pkl"))
        df_tokenized_val.to_pickle(os.path.join(self.writeDir, "df_tokenized_val.pkl"))
        df_tokenized_test.to_pickle(os.path.join(self.writeDir, "df_tokenized_test.pkl"))


    def setup(self, stage = None):
        if (stage == "fit") or (stage is None):
            df_tokenized_train = pd.read_pickle(os.path.join(self.writeDir, "df_tokenized_train.pkl"))
            df_tokenized_val = pd.read_pickle(os.path.join(self.writeDir, "df_tokenized_val.pkl"))
            self.train_data = CustomDataset(dataframe = df_tokenized_train)
            self.val_data = CustomDataset(dataframe = df_tokenized_val)
        if (stage == "test") or (stage is None):
            df_tokenized_test = pd.read_pickle(os.path.join(self.writeDir, "df_tokenized_test.pkl"))
            self.test_data = CustomDataset(dataframe = df_tokenized_test)

    def train_dataloader(self):
        train_dataloader = DataLoader(self.train_data, batch_size = self.train_bs, 
                                num_workers = self.num_cpu_workers, shuffle = True,
                                pin_memory = True, persistent_workers = True) 
        return train_dataloader

    def val_dataloader(self):
        val_dataloader = DataLoader(self.val_data, batch_size = self.eval_bs, 
                                num_workers = self.num_cpu_workers, shuffle = False,
                                pin_memory = True, persistent_workers = True) 
        return val_dataloader

    def test_dataloader(self):
        test_dataloader = DataLoader(self.test_data, batch_size = self.eval_bs, 
                                num_workers = self.num_cpu_workers, shuffle = False,
                                pin_memory = True, persistent_workers = True) 
        return test_dataloader

#================== MODEL ======================
def getTokenizer(tokenizer_name_or_path):
    tokenizer = RobertaTokenizer.from_pretrained(tokenizer_name_or_path)
    return tokenizer
    

class T5FineTuner(pl.LightningModule):
    def __init__(self, hparams, tokenizer):
        super(T5FineTuner, self).__init__()
        self.hparams.update(hparams)
        
        self.model = T5ForConditionalGeneration.from_pretrained(self.hparams.model_name_or_path)
        self.tokenizer = tokenizer
        self.UNK_IDX, self.PAD_IDX, self.BOS_IDX, self.EOS_IDX = \
                                        self.tokenizer.convert_tokens_to_ids(self.tokenizer.unk_token), \
                                        self.tokenizer.convert_tokens_to_ids(self.tokenizer.pad_token), \
                                        self.tokenizer.convert_tokens_to_ids(self.tokenizer.bos_token), \
                                        self.tokenizer.convert_tokens_to_ids(self.tokenizer.eos_token)
        self.loss_fn = torch.nn.CrossEntropyLoss(ignore_index = self.PAD_IDX, reduction='none')

        #https://github.com/huggingface/transformers/issues/12763
        self.model.resize_token_embeddings(len(self.tokenizer))
        self.TGT_VOCAB_SIZE = len(self.tokenizer)

        #metrics
        self.valid_mets = CodeQualityMetrics(self.tokenizer, self.hparams.writeDir, self.hparams.DEST_LANG)
        self.test_mets = CodeQualityMetrics(self.tokenizer, self.hparams.writeDir, self.hparams.DEST_LANG)

        self.testMetsDict_forCallback = {}

        #best val metrics
        #self.least_val_loss = [math.inf, False]
        #self.highest_val_compSucc = [-1, False]
    
    def forward(self, source_ids, source_mask=None, target_ids=None, target_mask=None):
        return self.model(
                input_ids=source_ids,
                attention_mask=source_mask,
                labels=target_ids, 
                decoder_attention_mask=target_mask)

    def _TRstep(self, src, dest, batch_idx, use_CF):
        outputs = self(source_ids = src,
                        source_mask = src.ne(self.tokenizer.pad_token_id),
                        target_ids = dest,
                        target_mask = dest.ne(self.tokenizer.pad_token_id)
                    )

        logits = outputs.logits
        logits = torch.transpose(logits, 0, 1)
        pred_tokens_ids = torch.argmax(logits, dim=2)

        #print ("pred_tokens_ids", pred_tokens_ids)

        loss = self.loss_fn(logits.reshape(-1, logits.shape[-1]), torch.transpose(dest, 0, 1).reshape(-1))

        if self.hparams.PERFORMANCE_CHCK_FLAG:
            pr.enable()

        if use_CF:
            if (self.hparams.DEST_LANG == 'python'):              
                CFloss_allProgs = LT_utils_CFLoss.create_compiler_loss_forBatch(pred_tokens_ids.cpu().numpy(), 
                                                        'python', 
                                                        self.tokenizer, self.hparams.writeDir, 
                                                        self.BOS_IDX, False, str(self.global_rank))
            elif (self.hparams.DEST_LANG == 'java'):
                CFloss_allProgs = LT_utils_CFLoss.create_compiler_loss_forBatch(pred_tokens_ids.cpu().numpy(), 
                                                        'java', 
                                                        self.tokenizer, self.hparams.writeDir, 
                                                        self.BOS_IDX, False, str(self.global_rank))
            assert CFloss_allProgs.shape[0] * self.hparams.max_sent_len == loss.shape[0]
            CFloss_allProgs_rptNumTokTimes = np.repeat(CFloss_allProgs, int(loss.shape[0]/CFloss_allProgs.shape[0]))
            CFloss_tensor = torch.tensor(CFloss_allProgs_rptNumTokTimes, dtype=torch.float32).to(self.device)

            loss = (1 - self.hparams.cf_weight) * loss + self.hparams.cf_weight * CFloss_tensor

        if self.hparams.PERFORMANCE_CHCK_FLAG:
            pr.disable()

        return loss.mean()

    def training_step(self, batch, batch_idx):
        src, dest = batch[0], batch[1]
        start_time = timer()
        train_loss = self._TRstep(src, dest, batch_idx, use_CF = self.hparams.use_compiler_feedback)
        end_time = timer()
        self.log("train_loss", train_loss, on_step = False, on_epoch = True, prog_bar = True, sync_dist=True)
        return train_loss

    #def on_validation_epoch_start(self):
    #    self.valid_mets.reset()

    def validation_step(self, batch, batch_idx):
        #print ("\n\nDEVICE: ", self.device, "global_rank", self.global_rank)
        src, dest, probIDs = batch[0], batch[1], batch[2]
        pred_tokens_ids_fromModel = (self.model.generate(
                                        input_ids = src,
                                        attention_mask = src.ne(self.tokenizer.pad_token_id), 
                                        max_length = self.hparams.max_sent_len
                                    )).transpose(0, 1)
        pred_tokens_ids = torch.ones(self.hparams.max_sent_len, pred_tokens_ids_fromModel.shape[1], 
                                        dtype = torch.int64, device = self.device) * self.PAD_IDX 
        pred_tokens_ids[:pred_tokens_ids_fromModel.shape[0], :pred_tokens_ids_fromModel.shape[1]] = \
                                pred_tokens_ids_fromModel
        logits = torch.nn.functional.one_hot(pred_tokens_ids, num_classes = self.TGT_VOCAB_SIZE).to(torch.float32)
        loss = self.loss_fn(logits.reshape(-1, logits.shape[-1]), torch.transpose(dest, 0, 1).reshape(-1)).mean()
        mets = self.valid_mets(torch.t(pred_tokens_ids), loss, dest, probIDs,
                        batch_idx, self.current_epoch, str(self.global_rank))
        return loss
    
    def validation_epoch_end(self, outputs):
        metsDict = self.valid_mets.compute(dataPartition = "val", epochNum = self.current_epoch,
                                            deviceID = self.global_rank)
        '''
        if (not self.least_val_loss[1]) and (metsDict["val_loss"] <= self.least_val_loss[0]):
            self.least_val_loss = [metsDict["val_loss"], True]
        if (not self.highest_val_compSucc[1]) and \
                        (metsDict["val_compilation_succ"] >= self.highest_val_compSucc[0]):
            self.highest_val_compSucc = [metsDict["val_compilation_succ"], True]
        '''
        for key in metsDict:
            self.log(key, metsDict[key], on_step = False, on_epoch = True, 
                                    sync_dist = True, prog_bar = True)
        self.valid_mets.reset()

    def test_step(self, batch, batch_idx):
        src, dest, probIDs = batch[0], batch[1], batch[2]
        pred_tokens_ids_fromModel = (self.model.generate(
                                        input_ids = src,
                                        attention_mask = src.ne(self.tokenizer.pad_token_id), 
                                        max_length = self.hparams.max_sent_len
                                    )).transpose(0, 1)
        pred_tokens_ids = torch.ones(self.hparams.max_sent_len, pred_tokens_ids_fromModel.shape[1], 
                                        dtype = torch.int64, device = self.device) * self.PAD_IDX 
        pred_tokens_ids[:pred_tokens_ids_fromModel.shape[0], :pred_tokens_ids_fromModel.shape[1]] = \
                                pred_tokens_ids_fromModel
        logits = torch.nn.functional.one_hot(pred_tokens_ids, num_classes = self.TGT_VOCAB_SIZE).to(torch.float32)
        loss = self.loss_fn(logits.reshape(-1, logits.shape[-1]), torch.transpose(dest, 0, 1).reshape(-1)).mean()
        mets = self.test_mets(torch.t(pred_tokens_ids), loss, dest, probIDs,
                        batch_idx, self.current_epoch, str(self.global_rank))
        return loss
    
    def test_epoch_end(self, outputs):
        metsDict = self.test_mets.compute(dataPartition = "test", epochNum = -1,
                                            deviceID = self.global_rank)
        self.testMetsDict_forCallback = copy.deepcopy(metsDict)
        self.test_mets.reset()

    def configure_optimizers(self):
        #Prepare optimizer and schedule (linear warmup and decay)
        optimizer = torch.optim.Adam(self.parameters(), lr=0.0001, betas=(0.9, 0.98), eps=1e-9)
        return optimizer

class CustomTestCallback(pl.Callback):
    def on_test_epoch_start(self, trainer, pl_module):
        shutil.rmtree(os.path.join(pl_module.hparams.writeDir, "epoch_-1"), ignore_errors = True)

    def on_test_epoch_end(self, trainer, pl_module):
        global TEST_EPOCH_NUM
        pl_module.testMetsDict_forCallback["epoch"] = TEST_EPOCH_NUM

        trainer.logger.experiment.log(pl_module.testMetsDict_forCallback)
        pl_module.testMetsDict_forCallback = {}

        tmpEpoch_Path = os.path.join(pl_module.hparams.writeDir, "epoch_-1")
        fileList = [os.path.join(tmpEpoch_Path, f) 
                        for f in listdir(tmpEpoch_Path) 
                            if (isfile(join(tmpEpoch_Path, f)) and f.endswith(".txt"))]

        for filePath in fileList:
            newFilePath = filePath.replace("epoch_-1", "epoch_{}".format(TEST_EPOCH_NUM)).replace(
                                            "epoch-1", "epoch{}".format(TEST_EPOCH_NUM))
            newFolder = os.path.join(pl_module.hparams.writeDir, "epoch_{}".format(TEST_EPOCH_NUM))
            if not os.path.exists(newFolder): os.makedirs(newFolder, exist_ok = True)
            shutil.copyfile(filePath, newFilePath)

'''
class CustomValCallback(pl.Callback):
    def setup(self, trainer, pl_module, stage):
        if stage in ("fit", "validate"):
            # setup the predict data even for fit/validate, as we will call it during `on_validation_epoch_end`
            trainer.datamodule.setup("test")
            pass
    def on_validation_epoch_end(self, trainer, pl_module):
        if trainer.sanity_checking:  # optional skip
            return
        if (pl_module.least_val_loss[1] or pl_module.highest_val_compSucc[1]):
            print ("Either val-loss ({}) decreased or val-compilationSucc ({}) increased...Starting test".format(
                    pl_module.least_val_loss[0], pl_module.highest_val_compSucc[0]))
            test_dataloader = trainer._data_connector._test_dataloader_source.dataloader()
            trainer.test(pl_module, test_dataloader)
            pl_module.least_val_loss[1] = False
            pl_module.highest_val_compSucc[1] = False
'''

#================== MAIN ======================
if __name__ == '__main__':
    DEBUG_FLAG = False
    PERFORMANCE_CHCK_FLAG = False
    if PERFORMANCE_CHCK_FLAG:
        pr = cProfile.Profile()

    #--------------- SETTING SEED, CURRENT REPO AND ARGS ----------------
    set_seed(7)
    current_repo = os.path.abspath(os.getcwd()) or "./"
    args = argParse_helperFunc()

    #--------------- INITIALIZING TOKENIZER ----------------
    tokenizer = getTokenizer(os.path.join(args.writeDir, "tokenizer"))

    #--------------- TRAINING ----------------
    train_bs = args.batch_size
    eval_bs = args.batch_size
    pathDict =  {
                'java2py':  {
                            'train_source': current_repo + '/AVATAR_data/data_LARGE/train.java-python.java',
                            'train_ref': current_repo + '/AVATAR_data/data_LARGE/train.java-python.python',
                            'train_id': current_repo + '/AVATAR_data/data_LARGE/train.java-python.id',
                            'val_source': current_repo + '/AVATAR_data/data_LARGE/valid.java-python.java',
                            'val_ref': current_repo + '/AVATAR_data/data_LARGE/valid.java-python.python',
                            'val_id': current_repo + '/AVATAR_data/data_LARGE/valid.java-python.id',
                            'test_source': current_repo + '/AVATAR_data/data_LARGE/test.java-python.java',
                            'test_ref': current_repo + '/AVATAR_data/data_LARGE/test.java-python.python',
                            'test_id': current_repo + '/AVATAR_data/data_LARGE/test.java-python.id'                         
                            },
                'py2java':  {
                            'train_source': current_repo + '/AVATAR_data/data_LARGE/train.java-python.python',
                            'train_ref': current_repo + '/AVATAR_data/data_LARGE/train.java-python.java',
                            'train_id': current_repo + '/AVATAR_data/data_LARGE/train.java-python.id',
                            'val_source': current_repo + '/AVATAR_data/data_LARGE/valid.java-python.python',
                            'val_ref': current_repo + '/AVATAR_data/data_LARGE/valid.java-python.java',
                            'val_id': current_repo + '/AVATAR_data/data_LARGE/valid.java-python.id',
                            'test_source': current_repo + '/AVATAR_data/data_LARGE/test.java-python.python',
                            'test_ref': current_repo + '/AVATAR_data/data_LARGE/test.java-python.java',
                            'test_id': current_repo + '/AVATAR_data/data_LARGE/test.java-python.id'                               
                            },
                'java2py_debug':  {
                            'train_source': current_repo + '/AVATAR_data/data_SMALL/train.java-python.java',
                            'train_ref': current_repo + '/AVATAR_data/data_SMALL/train.java-python.python',
                            'train_id': current_repo + '/AVATAR_data/data_SMALL/train.java-python.id',
                            'val_source': current_repo + '/AVATAR_data/data_SMALL/valid.java-python.java',
                            'val_ref': current_repo + '/AVATAR_data/data_SMALL/valid.java-python.python',
                            'val_id': current_repo + '/AVATAR_data/data_SMALL/valid.java-python.id',
                            'test_source': current_repo + '/AVATAR_data/data_SMALL/test.java-python.java',
                            'test_ref': current_repo + '/AVATAR_data/data_SMALL/test.java-python.python',
                            'test_id': current_repo + '/AVATAR_data/data_SMALL/test.java-python.id'                            
                            },
                'py2java_debug':  {
                            'train_source': current_repo + '/AVATAR_data/data_SMALL/train.java-python.python',
                            'train_ref': current_repo + '/AVATAR_data/data_SMALL/train.java-python.java',
                            'train_id': current_repo + '/AVATAR_data/data_SMALL/train.java-python.id',
                            'val_source': current_repo + '/AVATAR_data/data_SMALL/valid.java-python.python',
                            'val_ref': current_repo + '/AVATAR_data/data_SMALL/valid.java-python.java',
                            'val_id': current_repo + '/AVATAR_data/data_SMALL/valid.java-python.id',
                            'test_source': current_repo + '/AVATAR_data/data_SMALL/test.java-python.python',
                            'test_ref': current_repo + '/AVATAR_data/data_SMALL/test.java-python.java',
                            'test_id': current_repo + '/AVATAR_data/data_SMALL/test.java-python.id'                          
                            }
                }

    data_module = CodeTranslationDataModule(args.src_lang, args.dest_lang, 
                        tokenizer,
                        pathDict, args.writeDir, DEBUG_FLAG,
                        train_bs, eval_bs, args.num_cpu_workers)

    model_hparams = {   
                        'model_name_or_path': 'Salesforce/codet5-base',
                        'max_sent_len': 512,
                        'SRC_LANG': args.src_lang,
                        'DEST_LANG': args.dest_lang,
                        'use_compiler_feedback': bool(args.cf_mode),
                        'cf_weight': args.cf_weight,
                        'writeDir': args.writeDir,
                        'genericValSavePath': '{}_valPredictions'.format(args.dest_lang),
                        'genericTestSavePath': '{}_testPredictions'.format(args.dest_lang),
                        'train_bs': train_bs,
                        'eval_bs': eval_bs,
                        'DEBUG_FLAG': DEBUG_FLAG,
                        'PERFORMANCE_CHCK_FLAG': PERFORMANCE_CHCK_FLAG,
                        'valRefPath': data_module.valRefPath,
                        'testRefPath': data_module.testRefPath
                    }
    model = T5FineTuner(model_hparams, tokenizer)
    modelSavePath = os.path.join(args.writeDir, "models")

    #pl.loggers.WandbLogger.require("service")
    wanDB_logger = pl.loggers.WandbLogger(save_dir = args.writeDir, 
                        project = "program-translation", entity = "translation-vg",
                        tags = [args.model_name, args.model_tag, f"{args.src_lang}2{args.dest_lang}"], 
                        notes = args.model_notes, settings=wandb.Settings(start_method='fork'), 
                        save_code = True, 
                        config = args)
    wanDB_logger.experiment.name = args.model_name


    # Initialising Checkpoints
    #https://devblog.pytorchlightning.ai/introducing-multiple-modelcheckpoint-callbacks-e4bc13f9c185
    checkpoint_callback_vLoss = pl.callbacks.ModelCheckpoint(
        monitor = 'val_runtimeEquiv_succ', #val_loss
        dirpath = modelSavePath,
        filename = 'vRunEquivChckpt-{epoch}-{val_runtimeEquiv_succ:.3f}-{val_compilation_succ:.3f}' +\
                    '-{val_mean_errStrtByProgLen:.3f}',
        save_top_k = 2,
        every_n_epochs = 2,
        save_last = True,
        mode = "max" #min
        )
    checkpoint_callback_vLoss.CHECKPOINT_NAME_LAST = "{epoch}-last"

    checkpoint_callback_vCompSucc = pl.callbacks.ModelCheckpoint(
        monitor = 'val_compilation_succ',
        dirpath = modelSavePath,
        filename = 'vCompSuccChckpt-{epoch}-{val_runtimeEquiv_succ:.3f}-{val_compilation_succ:.3f}' +\
                    '-{val_mean_errStrtByProgLen:.3f}',
        save_top_k = 2,
        every_n_epochs = 2,
        save_last = False,
        mode = "max"
        )

    checkpoint_callback_vFirstErrorScore = pl.callbacks.ModelCheckpoint(
        monitor = 'val_mean_errStrtByProgLen',
        dirpath = modelSavePath,
        filename = 'vFrstErrScoreChckpt-{epoch}-{val_runtimeEquiv_succ:.3f}-{val_compilation_succ:.3f}' +\
                    '-{val_mean_errStrtByProgLen:.3f}',
        save_top_k = 2,
        every_n_epochs = 2,
        save_last = False,
        mode = "max"
        )

    earlyStopping_callback = pl.callbacks.early_stopping.EarlyStopping(
        monitor = "val_mean_errStrtByProgLen", 
        patience = 20, 
        verbose = True, 
        mode = "max"
        )

    # Training model
    trainer = pl.Trainer(precision=16, accelerator = "gpu", num_nodes = args.num_nodes, 
                            devices = args.num_gpus_per_node, 
                            strategy = "ddp_find_unused_parameters_false", 
                            max_epochs = args.num_epochs, logger = wanDB_logger,
                            check_val_every_n_epoch = 2,
                            callbacks = [checkpoint_callback_vLoss, checkpoint_callback_vCompSucc,
                                        checkpoint_callback_vFirstErrorScore,
                                        earlyStopping_callback, CustomTestCallback()]) #CustomTestCallback(), CustomValCallback()
    trainer.fit(model, data_module)
    trainer.strategy.barrier() # all processes meet

    # Test model on best checkpoints
    print ("\n\nStarting to Test...")
    #trainer = pl.Trainer(precision=16, accelerator = "gpu", devices = 1, nodes = 1,
    #                        strategy = "ddp_find_unused_parameters_false", 
    #                        logger = wanDB_logger,
    #                        callbacks = [CustomTestCallback()])
    ckptList = [f for f in listdir(modelSavePath) if (isfile(join(modelSavePath, f)) and 
                                                        f.endswith(".ckpt"))]
    uniqueCkptList = {}
    for ckptNm in ckptList:
        epNum = re.findall("epoch=(\d+)", ckptNm)[0]
        if epNum not in uniqueCkptList:
            uniqueCkptList[epNum] = os.path.join(modelSavePath, ckptNm)
    #print ("\n\nuniqueCkptList: ", uniqueCkptList, "\n\n")
    for key in uniqueCkptList: 
        print ("\n\nTesting ckpt of epoch {} on the dataset, path {}\n\n".format(key, uniqueCkptList[key]))
        TEST_EPOCH_NUM = int(key)
        trainer.test(model = model, dataloaders = data_module, ckpt_path = uniqueCkptList[key])