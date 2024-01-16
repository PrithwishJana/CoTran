import torch
from transformers import AutoTokenizer
from transformers import RobertaTokenizer, T5ForConditionalGeneration
from trl import PPOTrainer, PPOConfig
from trl import AutoModelForSeq2SeqLMWithValueHead, AutoModelForCausalLMWithValueHead, create_reference_model, set_seed
from trl.core import respond_to_batch
import os, random, argparse, sys, copy
import numpy as np
import pandas as pd
from datasets import Dataset
from torch.utils.data import DataLoader
from tqdm import tqdm
from language_translation_RLrewards import calculateCompilerReward
from accelerate import Accelerator

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
    return tokenizer.encode(code, truncation = True, padding = 'max_length', 
                            max_length=750, return_tensors = 'np')

def collator(data):
    #print ("ddata")
    return dict((key, [d[key] for d in data]) for key in data[0])

#=================== SETTING ARGPARSE ARGUMENTS ====================
def argParse_helperFunc():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, required=False, default="python2java_RL")
    parser.add_argument('--model_path', type=str, required=False, default="FINETUNED_MODELS")
    parser.add_argument('--src_lang', type=str, required=False, default="python", choices=["java", "python"])
    parser.add_argument('--dest_lang', type=str, required=False, default="java", choices=["java", "python"])
    parser.add_argument('--num_epochs', type=int, required=False, default=2)
    parser.add_argument('--train_batch_size', type=int, required=True, default=512)
    parser.add_argument('--test_batch_size', type=int, required=True, default=128)
    parser.add_argument('--writeDir', type=str, required=True)
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
    model = AutoModelForSeq2SeqLMWithValueHead.from_pretrained(model)
    return model

#================== DATASET ======================
def getDataset(path_dict, tokenizer):
    path_AVATAR_training_data_source = path_dict['train_source']
    path_AVATAR_training_data_reference = path_dict['train_ref']
    path_AVATAR_training_data_id = path_dict['train_id']
    path_AVATAR_validate_data_source = path_dict['val_source']
    path_AVATAR_validate_data_reference = path_dict['val_ref']
    path_AVATAR_validate_data_id = path_dict['val_id']
    path_AVATAR_test_data_source = path_dict['test_source']
    path_AVATAR_test_data_reference = path_dict['test_ref']
    path_AVATAR_test_data_id = path_dict['test_id']

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

    tokenized_train = [(tokenize_code(sample[0], tokenizer).flatten(),
                        tokenize_code(sample[1], tokenizer).flatten(),
                         0) for 
                    sample in training_dataset[:20000]] #NOTE: put 0 instead of  sample[2], to reduce memory
    #NOTE: dataset reduced to 20k
    tokenized_val = [(tokenize_code(sample[0], tokenizer).flatten(),
                        tokenize_code(sample[1], tokenizer).flatten(),
                        sample[2]) for
                    sample in validate_dataset]
    tokenized_test = [(tokenize_code(sample[0], tokenizer).flatten(),
                        tokenize_code(sample[1], tokenizer).flatten(),
                        sample[2]) for
                    sample in test_dataset]

    df_tokenized_train = pd.DataFrame(tokenized_train, columns=["input_ids_src", "input_ids_tgt", "probID"])
    df_tokenized_val = pd.DataFrame(tokenized_val, columns=["input_ids_src", "input_ids_tgt", "probID"])
    df_tokenized_test = pd.DataFrame(tokenized_test, columns=["input_ids_src", "input_ids_tgt", "probID"])

    df_tokenized_train.to_csv(os.path.join(args.writeDir, "df_tokenized_train.csv"), 
                                        encoding='utf-8')
    df_tokenized_val.to_csv(os.path.join(args.writeDir, "df_tokenized_val.csv"), 
                                        encoding='utf-8')
    df_tokenized_test.to_csv(os.path.join(args.writeDir, "df_tokenized_test.csv"), 
                                        encoding='utf-8')    

    modifiedPrint("\n----- Train DataFrame -----\n")
    modifiedPrint(df_tokenized_train.iloc[0]["input_ids_src"].shape)
    modifiedPrint(df_tokenized_train)

    modifiedPrint("\n----- Valid DataFrame -----\n")
    modifiedPrint(df_tokenized_val.iloc[0]["input_ids_src"].shape)
    modifiedPrint(df_tokenized_val)

    modifiedPrint("\n----- Test DataFrame -----\n")
    modifiedPrint(df_tokenized_test.iloc[0]["input_ids_src"].shape)
    modifiedPrint(df_tokenized_test)

    dataset_train_val_test = [Dataset.from_pandas(x) for x in 
                                [df_tokenized_train, df_tokenized_val, df_tokenized_test]]
    for d in dataset_train_val_test:
        d.set_format("pytorch")

    return dataset_train_val_test[0], dataset_train_val_test[1], dataset_train_val_test[2]

def test(dataloader, model, kwargs, tokenizer, epoch, device):
    testOut = []
    for test_batch in tqdm(dataloader):
        src_id_mat = test_batch["input_ids_src"]
        print ("src_id_mat", src_id_mat)
        print ("src_id_mat.shape", src_id_mat.shape)
        #attention_mask_mat = src_id_mat.ne(tokenizer.pad_token_id)
        test_pred_idList = model.generate(src_id_mat.to(device), 
                                            **kwargs) #attention_mask = attention_mask_mat.to(device),
        test_pred_list = tokenizer.batch_decode(test_pred_idList, skip_special_tokens = True,
                                        clean_up_tokenization_spaces = False)
        testOut.extend(test_pred_list)
    #save
    #print (testOut)
    with open(os.path.join(args.writeDir, "result_ep{}_dev{}.txt".format(epoch, str(device))), 
                'w', encoding = 'utf-8') as f:
        for line in testOut:
            f.write(f"{line}\n")

#================== MAIN ======================
if __name__ == '__main__':
    DEBUG_FLAG = False

    #--------------- SETTING SEED, CURRENT REPO AND ARGS ----------------
    setSeed(7)
    current_repo = os.path.abspath(os.getcwd()) or "./"
    args = argParse_helperFunc()

    #--------------- INITIALIZING TOKENIZER ----------------
    fwdTok_LoadPath = os.path.join(args.model_path, 
                            args.src_lang + "2" + args.dest_lang, "tokenizer")
    fwdTokenizer = loadTokenizer(fwdTok_LoadPath)
    #print ("TOK:\n", fwdTokenizer)

    #--------------- INITIALIZING MODEL ----------------
    #device_map = {"": Accelerator().local_process_index}
    fwdModel_LoadPath = os.path.join(args.model_path, 
                            args.src_lang + "2" + args.dest_lang, "bestModel.ckpt")
    fwdModel = loadModelFromCkpt(fwdModel_LoadPath, fwdTokenizer) #, device_map
    fwdModel_ref = create_reference_model(fwdModel)
    #print (fwdModel)

    #--------------- INITIALIZING DATASET ----------------
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
    fwdDataset_train_val_test = getDataset(pathDict[args.src_lang + "2" + args.dest_lang], 
                                        fwdTokenizer) # + "_debug"
    tester_dataloader = DataLoader(fwdDataset_train_val_test[2], batch_size = args.test_batch_size)
    train_dataloader = DataLoader(fwdDataset_train_val_test[0], batch_size = args.train_batch_size)
    print (fwdDataset_train_val_test)

    #--------------- RL ----------------
    ppo_config = PPOConfig(
        steps=20000, learning_rate=1.41e-5, remove_unused_columns=False, 
        batch_size = args.train_batch_size, log_with="wandb") #, log_with="wandb" NOTE!!!!!!!!!!!!!!

    print ("dataset len", len(fwdDataset_train_val_test[0]))

    ppo_trainer = PPOTrainer(config = ppo_config, 
                                model = fwdModel, 
                                ref_model = fwdModel_ref, 
                                tokenizer = fwdTokenizer
                            ) #TODO: data_collator=collator needed here????, 
                            #dataset = fwdDataset_train_val_test[0]

    print ("ppo_trainer.dataloader len", len(train_dataloader))

    # Multi-GPU can be used using https://huggingface.co/docs/trl/main/en/customization
    if ppo_trainer.accelerator.num_processes == 1:
        device = 0 if torch.cuda.is_available() else "cpu"  # to avoid a `pipeline` bug
    else:
        device = ppo_trainer.accelerator.device

    train_dataloader = ppo_trainer.accelerator.prepare(train_dataloader)

    print ("DEVICE", device)

    generation_kwargs = {
        "min_length": -1, # don't ignore the EOS token (see above)
        "top_k": 0.0, # no top-k sampling
        "top_p": 1.0, # no nucleus sampling
        "do_sample": True, # yes, we want to sample
        "pad_token_id": fwdTokenizer.pad_token_id, # most decoder models don't have a padding token - use EOS token instead
        "max_new_tokens": 750
    }
    #"max_new_tokens": 32, # specify how many tokens you want to generate at most
    #"max_length": 750 (dauntless-planet-49)

    test_kwargs = {
        "do_sample": False,
        "max_new_tokens": 750
    }

    if args.dest_lang == "java":
        generation_kwargs["bad_words_ids"] = [[32116], [32117], [32118]]
        test_kwargs["bad_words_ids"] = [[32116], [32117], [32118]]

    #test(tester_dataloader, fwdModel, test_kwargs, fwdTokenizer, "init", device)
    #UNCOMMENT LATER




    #f.write(f"{line}\n")
    #UnicodeEncodeError: 'ascii' codec can't encode character '\u2581' in position 1015: ordinal not in range(128)

    for epoch in range(args.num_epochs):
        #TODO: where to set bs
        for batch in tqdm(train_dataloader):
            #print ("bbatch", batch)
            cotran = dict()
            src_id_mat = batch["input_ids_src"] #--> torch.Size([8, 512])
            #attention_mask_mat = src_id_mat.ne(fwdTokenizer.pad_token_id)

            #print ("src_id_mat", src_id_mat)
            #print ("src_id_mat.shape", src_id_mat.shape) 

            src_id_list = list(src_id_mat)
            #attention_mask_list = list(attention_mask_mat)
            #--> list of len 8, each elem is a torch array of size 512
            # these are the tokenized input to be fed to the CodeT5-model
            
            #print ("src_id_list", src_id_list)
            #print ("src_id_list.shape", len(src_id_list), src_id_list[0].shape) 
            
            tgtPred_id_list = ppo_trainer.generate(src_id_list, 
                                                    **generation_kwargs) #attention_mask = attention_mask_list,
            #--> list of len 8, each elem is a torch array of size 512
            # these are the tokenized predicted output from the CodeT5-model

            #print ("tgtPred_id_list", tgtPred_id_list)
            #print ("tgtPred_id_list.shape", tgtPred_id_list.shape)

            tgtPred_list = fwdTokenizer.batch_decode(tgtPred_id_list, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False)

            #print ("tgtPred_list", tgtPred_list)

            # Calculate reward
            rewards = calculateCompilerReward(tgtPred_list, args.dest_lang, 
                                            args.writeDir, str(tgtPred_id_list[0].get_device()))
            #rewards = [torch.tensor(1.0) for i in range(args.batch_size)]

            #### Run PPO step
            stats = ppo_trainer.step(src_id_list, tgtPred_id_list, rewards) # train using PPO
            ppo_trainer.log_stats(stats, batch, rewards) # wandb integrated
    
        #testing
        test(tester_dataloader, fwdModel, test_kwargs, fwdTokenizer, epoch, device)

        
