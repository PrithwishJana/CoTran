import torch
from transformers import AutoTokenizer
from transformers import RobertaTokenizer, T5ForConditionalGeneration, AutoModelForSeq2SeqLM
from trl import PPOTrainer, PPOConfig
from trl import AutoModelForSeq2SeqLMWithValueHead, create_reference_model, set_seed
from trl.core import respond_to_batch
import os, random, argparse, sys, copy
import numpy as np
import pandas as pd
from datasets import Dataset, DatasetDict
from torch.utils.data import DataLoader
from tqdm import tqdm
import shutil
from language_translation_RLrewards import calculateCompilerReward, calculateRuntimeReward, \
                        calculateCompilerRewardModified, calcCodeBLEUreward, \
                        calcCodeBLEUrewardWithMinLenPenalty
from accelerate import Accelerator
from peft import LoraConfig, TaskType, get_peft_model

from transformers import TrainingArguments, Seq2SeqTrainingArguments, Seq2SeqTrainer, DataCollatorForSeq2Seq
from trl import SFTTrainer

#os.environ["WANDB_DISABLED"] = "true"

current_repo = os.path.abspath(os.getcwd()) or "./"
pathDict =  {
            'java2python':  {
                        'train_source': current_repo + '/AVATAR-TC/train.java-python.java',
                        'train_ref': current_repo + '/AVATAR-TC/train.java-python.python',
                        'train_id': current_repo + '/AVATAR-TC/train.java-python.id',
                        'val_source': current_repo + '/AVATAR-TC/valid.java-python.java',
                        'val_ref': current_repo + '/AVATAR-TC/valid.java-python.python',
                        'val_id': current_repo + '/AVATAR-TC/valid.java-python.id',
                        'test_source': current_repo + '/AVATAR-TC/test.java-python.java',
                        'test_ref': current_repo + '/AVATAR-TC/test.java-python.python',
                        'test_id': current_repo + '/AVATAR-TC/test.java-python.id'                         
                        },
            'python2java':  {
                        'train_source': current_repo + '/AVATAR-TC/train.java-python.python',
                        'train_ref': current_repo + '/AVATAR-TC/train.java-python.java',
                        'train_id': current_repo + '/AVATAR-TC/train.java-python.id',
                        'val_source': current_repo + '/AVATAR-TC/valid.java-python.python',
                        'val_ref': current_repo + '/AVATAR-TC/valid.java-python.java',
                        'val_id': current_repo + '/AVATAR-TC/valid.java-python.id',
                        'test_source': current_repo + '/AVATAR-TC/test.java-python.python',
                        'test_ref': current_repo + '/AVATAR-TC/test.java-python.java',
                        'test_id': current_repo + '/AVATAR-TC/test.java-python.id'                               
                        },
            'java2python_debug':  {
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
            'python2java_debug':  {
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

def setSeed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    set_seed(seed)

def modifiedPrint(*stringsToPrint):
    for arg in stringsToPrint:
        print (arg, end=" ", flush=True)
    print ("", flush=True)

def tokenize_code(code, tokenizer):
    return tokenizer.encode(code, return_tensors = 'np', max_length=750, truncation = True)

def tokenize_code_maxLenPadding(code, tokenizer):
    return tokenizer.encode(code, truncation = True, padding = 'max_length', 
                            max_length=750, return_tensors = 'np')

#=================== SETTING ARGPARSE ARGUMENTS ====================
def argParse_helperFunc():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, required=False, default="python2java_RL")
    parser.add_argument('--model_path', type=str, required=False, default="FINETUNED_MODELS")
    parser.add_argument('--src_lang', type=str, required=False, default="python", choices=["java", "python"])
    parser.add_argument('--dest_lang', type=str, required=False, default="java", choices=["java", "python"])
    parser.add_argument('--num_epochs', type=int, required=False, default=2)
    parser.add_argument('--train_batch_size', type=int, required=False, default=512)
    parser.add_argument('--test_batch_size', type=int, required=False, default=128)
    parser.add_argument('--writeDir', type=str, required=True)
    parser.add_argument('--multigpu', type=bool, default=False)
    args = parser.parse_args()
    modifiedPrint(args)
    return args

#================== TOKENIZER & MODEL ======================
def loadTokenizer(tokenizer_name_or_path):
    tokenizer = RobertaTokenizer.from_pretrained(tokenizer_name_or_path)
    #tokenizer.pad_token = tokenizer.eos_token
    return tokenizer

def loadModelFromCkpt(model_path, tokenizer):
    ckpt = torch.load(model_path, map_location='cpu')["state_dict"]
    ckpt = dict((key.replace("model.", ""), value) for (key, value) in ckpt.items())
    model = T5ForConditionalGeneration.from_pretrained("Salesforce/codet5-base")
    model.resize_token_embeddings(len(tokenizer))
    model.load_state_dict(ckpt)
    return model

#================== DATASET ======================
def collator(data):
    #Collator input: [{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}]
    #Collator output: {'key1': ['value1'], 'key2': ['value2'], 'key3': ['value3']}
    return dict((key, [d[key] for d in data]) for key in data[0])

def getDataset(path_dict, tokenizer, srcLang = "python"):
    path_AVATAR_training_data_source = path_dict['train_source']
    path_AVATAR_training_data_reference = path_dict['train_ref']
    path_AVATAR_training_data_id = path_dict['train_id']
    path_AVATAR_validate_data_source = path_dict['val_source']
    path_AVATAR_validate_data_reference = path_dict['val_ref']
    path_AVATAR_validate_data_id = path_dict['val_id']
    path_AVATAR_test_data_source = path_dict['test_source']
    path_AVATAR_test_data_reference = path_dict['test_ref']
    path_AVATAR_test_data_id = path_dict['test_id']
    if (srcLang == "java"):
        path_AVATAR_training_data_source, path_AVATAR_training_data_reference = \
                        path_AVATAR_training_data_reference, path_AVATAR_training_data_source
        path_AVATAR_validate_data_source, path_AVATAR_validate_data_reference = \
                        path_AVATAR_validate_data_reference, path_AVATAR_validate_data_source
        path_AVATAR_test_data_source, path_AVATAR_test_data_reference = \
                        path_AVATAR_test_data_reference, path_AVATAR_test_data_source

    #------------------ READING DATA ------------------
    src_training_data = []
    dest_training_data = []
    ids_training = []
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

    with open(path_AVATAR_training_data_id, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            ids_training.append(line.strip().replace("\t", "    "))
        f.close()

    assert len(src_training_data) == len(dest_training_data)
    assert len(dest_training_data) == len(ids_training)
    training_dataset = list(zip(src_training_data, dest_training_data, ids_training))

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

    tokenized_train = []
    for sample in training_dataset: #NOTE: [:10000] dataset reduced
        tokenizedSrc = tokenize_code(sample[0], tokenizer).flatten()
        tokenizedTgt = tokenize_code(sample[1], tokenizer).flatten()
        tokenized_train.append((tokenizedSrc,
                                sample[0],
                                (tokenizedSrc != tokenizer.pad_token_id) * 1,
                                tokenizedTgt,
                                sample[1],
                                sample[2]))

    tokenized_val = []
    for sample in validate_dataset: 
        tokenizedSrc = tokenize_code_maxLenPadding(sample[0], tokenizer).flatten()
        tokenizedTgt = tokenize_code_maxLenPadding(sample[1], tokenizer).flatten()
        tokenized_val.append((tokenizedSrc,
                                sample[0],
                                (tokenizedSrc != tokenizer.pad_token_id) * 1,
                                tokenizedTgt,
                                sample[1],
                                sample[2]))

    tokenized_test = []
    for sample in test_dataset: 
        tokenizedSrc = tokenize_code_maxLenPadding(sample[0], tokenizer).flatten()
        tokenizedTgt = tokenize_code_maxLenPadding(sample[1], tokenizer).flatten()
        tokenized_test.append((tokenizedSrc,
                                sample[0],
                                (tokenizedSrc != tokenizer.pad_token_id) * 1,
                                tokenizedTgt,
                                sample[1],
                                sample[2]))

    df_tokenized_train = pd.DataFrame(tokenized_train, columns=["input_ids", "query", 
                                                                "attention_mask",
                                                                "labels", "response_gt",
                                                                "probID"])
    df_tokenized_val = pd.DataFrame(tokenized_val, columns=["input_ids", "query", 
                                                                "attention_mask",
                                                                "labels", "response_gt",
                                                                "probID"])
    df_tokenized_test = pd.DataFrame(tokenized_test, columns=["input_ids", "query", 
                                                                "attention_mask",
                                                                "labels", "response_gt",
                                                                "probID"])

    df_tokenized_train.to_csv(os.path.join(args.writeDir, "df_tokenized_train.csv"), 
                                        encoding='utf-8')
    df_tokenized_val.to_csv(os.path.join(args.writeDir, "df_tokenized_val.csv"), 
                                        encoding='utf-8')
    df_tokenized_test.to_csv(os.path.join(args.writeDir, "df_tokenized_test.csv"), 
                                        encoding='utf-8')

    modifiedPrint("\n----- Train DataFrame -----\n")
    modifiedPrint(df_tokenized_train.iloc[0]["input_ids"].shape)
    modifiedPrint(df_tokenized_train)

    modifiedPrint("\n----- Valid DataFrame -----\n")
    modifiedPrint(df_tokenized_val.iloc[0]["input_ids"].shape)
    modifiedPrint(df_tokenized_val)

    modifiedPrint("\n----- Test DataFrame -----\n")
    modifiedPrint(df_tokenized_test.iloc[0]["input_ids"].shape)
    modifiedPrint(df_tokenized_test)

    dataset_train_val_test = [Dataset.from_pandas(x) for x in 
                                [df_tokenized_train, df_tokenized_val, df_tokenized_test]]
    for d in dataset_train_val_test:
        d.set_format(type = "torch")
    dd = DatasetDict({"train" : dataset_train_val_test[0],
                        "val" : dataset_train_val_test[1],
                        "test" : dataset_train_val_test[2]})
    print (dd)
    return dd

def test(dataloader, model, kwargs, tokenizer, epoch, device, targetLang = "java"):
    testOut = []
    for test_batch in tqdm(dataloader):
        if targetLang == "java":
            src_id_mat = test_batch["input_ids"]
        else:
            src_id_mat = test_batch["labels"]
        print ("src_id_mat", src_id_mat)
        print ("src_id_mat.shape", src_id_mat.shape)
        #attention_mask_mat = src_id_mat.ne(tokenizer.pad_token_id)
        test_pred_idList = model.generate(input_ids = src_id_mat.to(device), 
                                            **kwargs) #attention_mask = attention_mask_mat.to(device),
        test_pred_list = tokenizer.batch_decode(test_pred_idList, skip_special_tokens = True,
                                        clean_up_tokenization_spaces = False)
        testOut.extend(test_pred_list)

    with open(os.path.join(args.writeDir, "result_ep{}_dev{}.{}".format(epoch, str(device), targetLang)), 
                'w', encoding = 'utf-8') as f:
        for line in testOut:
            line = line.encode("unicode_escape").decode("utf-8")
            f.write(f"{line}\n")
            
def SFTTrain(model, tokenizer, datasetDict, writeDir):
    sft_training_args = Seq2SeqTrainingArguments(
        output_dir = writeDir, # output directory
        num_train_epochs = 2, # total number of training epochs
        per_device_train_batch_size = 8, # batch size per device during training
        logging_steps = 10,
        save_strategy = "no",
        save_total_limit = 1,
        do_train = True,
        do_eval = False,
        fp16 = True
    )
    print (datasetDict["train"][0])
    sft_trainer = Seq2SeqTrainer(
        model = model,
        args = sft_training_args,
        train_dataset = datasetDict["train"], # training dataset requires column input_ids
        data_collator = DataCollatorForSeq2Seq(tokenizer = tokenizer, model = model),
        tokenizer = tokenizer
    )
    sft_trainer.train()

def RLTrain(fmodel, ftokenizer, bmodel, btokenizer, datasetDict, writeDir, epOuter):
    global tester_dataloader, fwd_test_kwargs, bkwd_test_kwargs
    os.makedirs(os.path.join(args.writeDir, "model"), exist_ok = True)
    peft_config = LoraConfig(
        r = 16, # Rank
        lora_alpha = 32,
        target_modules = ["q", "v"],
        lora_dropout = 0.05,
        bias = "none",
        inference_mode = False, 
        task_type = TaskType.SEQ_2_SEQ_LM # FLAN-T5
    )
    fPmodel = get_peft_model(fmodel, peft_config)
    fPmodel.print_trainable_parameters()
    bPmodel = get_peft_model(bmodel, peft_config)
    bPmodel.print_trainable_parameters()
    
    fwdModel = AutoModelForSeq2SeqLMWithValueHead.from_pretrained(fPmodel,
                                        peft_config = peft_config, load_in_8bit = True)
    fwdModel_ref = create_reference_model(fwdModel)
    bkwdModel = AutoModelForSeq2SeqLMWithValueHead.from_pretrained(bPmodel,
                                        peft_config = peft_config, load_in_8bit = True)
    bkwdModel_ref = create_reference_model(bkwdModel)

    fwdPPO_config = PPOConfig(
        learning_rate=1.41e-5, remove_unused_columns = False, 
        batch_size = 2, log_with="wandb") #, batch_size = 512,, log_with="wandb" NOTE!!!!!!!!!!!!!!
    bkwdPPO_config = PPOConfig(
        learning_rate=1.41e-5, remove_unused_columns = False, 
        batch_size = 2, log_with="wandb") #, batch_size = 512,, log_with="wandb" NOTE!!!!!!!!!!!!!!

    fwdPPO_trainer = PPOTrainer(config = fwdPPO_config, 
                                model = fwdModel, 
                                ref_model = fwdModel_ref, 
                                tokenizer = ftokenizer,
                                dataset = datasetDict["train"],
                                data_collator = collator
                            )
    bkwdPPO_trainer = PPOTrainer(config = bkwdPPO_config, 
                                model = bkwdModel, 
                                ref_model = bkwdModel_ref, 
                                tokenizer = btokenizer,
                                dataset = datasetDict["train"],
                                data_collator = collator
                            )

    # Multi-GPU can be used using https://huggingface.co/docs/trl/main/en/customization
    if fwdPPO_trainer.accelerator.num_processes == 1:
        device = 0 if torch.cuda.is_available() else "cpu"  # to avoid a `pipeline` bug
    else:
        device = fwdPPO_trainer.accelerator.device

    fwd_generation_kwargs = {
        "min_length": -1, # don't ignore the EOS token (see above)
        "top_k": 0.0, # no top-k sampling
        "top_p": 1.0, # no nucleus sampling
        "do_sample": True, # yes, we want to sample
        "pad_token_id": ftokenizer.pad_token_id, # most decoder models don't have a padding token - use EOS token instead
        "eos_token_id": ftokenizer.eos_token_id,
        "max_new_tokens": 750
    }

    bkwd_generation_kwargs = {
        "min_length": -1, # don't ignore the EOS token (see above)
        "top_k": 0.0, # no top-k sampling
        "top_p": 1.0, # no nucleus sampling
        "do_sample": True, # yes, we want to sample
        "pad_token_id": btokenizer.pad_token_id, # most decoder models don't have a padding token - use EOS token instead
        "eos_token_id": btokenizer.eos_token_id,
        "max_new_tokens": 750,
        "bad_words_ids": [[32116], [32117], [32118]]
    }

    for epoch in range(2):
        training_dataloader = fwdPPO_trainer.dataloader
        for batch in tqdm(training_dataloader):
            src_id_mat = batch["input_ids"] #--> torch.Size([8, 512])
            tgt_id_mat = batch["labels"]
            src_id_list = list(src_id_mat)
            tgt_id_list = list(tgt_id_mat)

            probIDs = batch["probID"]

            tgtPred_id_list = fwdPPO_trainer.generate(src_id_list, 
                                                    **fwd_generation_kwargs) 
            srcPred_id_list = bkwdPPO_trainer.generate(tgtPred_id_list, 
                                                    **bkwd_generation_kwargs) 

            tgtPred_list = ftokenizer.batch_decode(tgtPred_id_list, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False)
            srcPred_list = btokenizer.batch_decode(srcPred_id_list, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False)
            tgt_list = batch["response_gt"]
            src_list = batch["query"]
            batch["response"] = tgtPred_list

            # Calculate fwd CF ---------
            fwdCompileRewards = calculateCompilerRewardModified(tgtPred_list, tgt_list,
                                            "python", 
                                            writeDir, str(tgtPred_id_list[0].get_device()))
            bkwdCompileRewards = calculateCompilerRewardModified(srcPred_list, src_list,
                                            "java", 
                                            writeDir, str(srcPred_id_list[0].get_device()))

            SF = calculateRuntimeRewardSF(srcPred_list, codeIDList, 
                            writeDir, str(tgtPred_id_list[0].get_device())) #new
            #---------
            # Calculate fwd BLEU ---------
            #fwdBLEURewards = calcCodeBLEUreward(tgtPred_list, tgt_list,
            #                                dest_lang, 
            #                                writeDir, str(tgtPred_id_list[0].get_device()))
            #fwdBLEURewards = calcCodeBLEUrewardWithMinLenPenalty(tgtPred_list, tgt_list,
            #                                dest_lang, 
            #                                writeDir, str(tgtPred_id_list[0].get_device())) 
            #---------

            print ("fCFRewards" + str(str(tgtPred_id_list[0].get_device())) + " " + str(fwdCompileRewards))
            print ("bCFRewards" + str(str(srcPred_id_list[0].get_device())) + " " + str(bkwdCompileRewards))

            #print ("BLEURewards" + str(str(tgtPred_id_list[0].get_device())) + " " + str(fwdBLEURewards))
            #print ("CombinedRewards" + str(str(tgtPred_id_list[0].get_device())) + " " + str(fwdReward))

            #### Run PPO step
            fwdStats = fwdPPO_trainer.step(src_id_list, tgtPred_id_list, fwdCompileRewards) # train using PPO
            fwdPPO_trainer.log_stats(fwdStats, batch, fwdCompileRewards + SF) # wandb integrated
            bkwdStats = bkwdPPO_trainer.step(tgtPred_id_list, srcPred_id_list, bkwdCompileRewards) # train using PPO
            bkwdPPO_trainer.log_stats(bkwdStats, batch, bkwdCompileRewards + SF) # wandb integrated
        if epoch % 1 == 0:
            test(tester_dataloader, fwdModel, fwd_test_kwargs, fwdTokenizer, 
                        str(epOuter) + "_" + str(epoch)+"fRL", 
                        device, "python")
            test(tester_dataloader, bkwdModel, bkwd_test_kwargs, bkwdTokenizer, 
                        str(epOuter) + "_" + str(epoch)+"bRL", 
                        device, "java")
    
    #print ("before", fwdModel)
    peft_fromFwdModel = fwdModel.pretrained_model
    fmergedModel = peft_fromFwdModel.merge_and_unload()
    #print ("pp", pp)
    fmergedModel.save_pretrained(os.path.join(args.writeDir, "fmodel"))
    ft5Model = T5ForConditionalGeneration.from_pretrained(os.path.join(args.writeDir, "fmodel"))

    #print ("before", fwdModel)
    peft_fromBkwdModel = bkwdModel.pretrained_model
    bmergedModel = peft_fromBkwdModel.merge_and_unload()
    #print ("pp", pp)
    bmergedModel.save_pretrained(os.path.join(args.writeDir, "bmodel"))
    bt5Model = T5ForConditionalGeneration.from_pretrained(os.path.join(args.writeDir, "bmodel"))
    
    #print ("ff", ff)
    #print ("hh", hh)
    #print ("after", fwdModel)
    if os.path.exists(os.path.join(args.writeDir, "fmodel")): 
        shutil.rmtree(os.path.join(args.writeDir, "bmodel"), ignore_errors=True)
    if os.path.exists(os.path.join(args.writeDir, "fmodel")): 
        shutil.rmtree(os.path.join(args.writeDir, "bmodel"), ignore_errors=True)
    return ft5Model, bt5Model, device


#================== MAIN ======================
if __name__ == '__main__':
    DEBUG_FLAG = False

    #--------------- SETTING SEED, CURRENT REPO AND ARGS ----------------
    setSeed(7) #UNCOMMENT?????????????????
    args = argParse_helperFunc()

    #--------------- INITIALIZING TOKENIZER ----------------
    fwdTok_LoadPath = os.path.join(args.model_path, 
                            args.src_lang + "2" + args.dest_lang, "tokenizer")
    fwdTokenizer = loadTokenizer(fwdTok_LoadPath)
    bkwdTok_LoadPath = os.path.join(args.model_path, 
                            args.dest_lang + "2" + args.src_lang, "tokenizer")
    bkwdTokenizer = loadTokenizer(bkwdTok_LoadPath)

    #--------------- INITIALIZING MODEL ----------------
    #device_map = {"": Accelerator().local_process_index}
    fwdModel_LoadPath = os.path.join(args.model_path, 
                            args.src_lang + "2" + args.dest_lang, "bestModel.ckpt")
    fmodel = loadModelFromCkpt(fwdModel_LoadPath, fwdTokenizer)
    bkwdModel_LoadPath = os.path.join(args.model_path, 
                            args.dest_lang + "2" + args.src_lang, "bestModel.ckpt")
    bmodel = loadModelFromCkpt(bkwdModel_LoadPath, bkwdTokenizer)

    #--------------- INITIALIZING DATASET ----------------
    fdatasetDict = getDataset(pathDict[args.src_lang + "2" + args.dest_lang + "_debug"], 
                                        fwdTokenizer) # + "_debug"
    tester_dataloader = DataLoader(fdatasetDict["test"], batch_size = args.test_batch_size, shuffle = False)
    bdatasetDict = getDataset(pathDict[args.dest_lang + "2" + args.src_lang + "_debug"], 
                                        bkwdTokenizer) # + "_debug"
    #--------------- RL ----------------
    fwd_test_kwargs = {
        "do_sample": False,
        "max_new_tokens": 750
    }

    bkwd_test_kwargs = {
        "do_sample": False,
        "max_new_tokens": 750,
        "bad_words_ids": [[32116], [32117], [32118]]
    }

    #--------------- CE-based FINETUNING ----------------
    print ("fmodel", fmodel)
    print ("bmodel", bmodel)

    #testing
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    fmodel = fmodel.to(device)
    bmodel = bmodel.to(device)
    #test(tester_dataloader, model, fwd_test_kwargs, fwdTokenizer, "init", device, args.dest_lang)

    #--------------- TRAINING LOOP ----------------
    for ep in range(10):
        fmodel, bmodel, device = RLTrain(fmodel, fwdTokenizer, 
                                bmodel, bkwdTokenizer, 
                                fdatasetDict, args.writeDir, ep)
        #test(tester_dataloader, model, fwd_test_kwargs, fwdTokenizer, str(ep)+"RL", device, args.dest_lang)
        SFTTrain(fmodel, fwdTokenizer, fdatasetDict, args.writeDir)
        SFTTrain(bmodel, bkwdTokenizer, bdatasetDict, args.writeDir)
        test(tester_dataloader, fmodel, fwd_test_kwargs, fwdTokenizer, str(ep)+"fSFT", device, args.dest_lang)
        test(tester_dataloader, bmodel, bkwd_test_kwargs, bkwdTokenizer, str(ep)+"bSFT", device, args.src_lang)
