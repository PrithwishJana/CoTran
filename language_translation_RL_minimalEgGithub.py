from transformers import RobertaTokenizer, T5ForConditionalGeneration
from trl import PPOTrainer, PPOConfig
from trl import AutoModelForSeq2SeqLMWithValueHead, create_reference_model
import pandas as pd
from datasets import Dataset, DatasetDict
from tqdm import tqdm
from accelerate import Accelerator
from peft import LoraConfig, TaskType, get_peft_model

def collator(data):
    return dict((key, [d[key] for d in data]) for key in data[0])

#--model + tokenizer--
model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
peft_config = LoraConfig(
    r=16, # Rank
    lora_alpha=32,
    target_modules=["q", "v"],
    lora_dropout=0.05,
    bias="none",
    inference_mode = False, 
    task_type = TaskType.SEQ_2_SEQ_LM # FLAN-T5
)

model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
model = AutoModelForSeq2SeqLMWithValueHead.from_pretrained(model, peft_config = peft_config)
model_ref = create_reference_model(model)

#--dataset--
dataset = [("My first query", "My first response"), ("My second query", "My second response"),
            ("My third query", "My third response"), ("My fourth query", "My fourth response")]
tokenized_dataset = [(sample[0],
                    (tokenizer.encode(sample[0], return_tensors = 'np')).flatten())
                   for sample in dataset]
df_tokenized_dataset = pd.DataFrame(tokenized_dataset, columns=["query", "query_ids"])
datasetCasted = Dataset.from_pandas(df_tokenized_dataset)
datasetCasted.set_format(type = "torch")
DDict = DatasetDict({"train" : datasetCasted})

print (DDict)

#--ppo--
PPO_config = PPOConfig(
    learning_rate=1.41e-5, remove_unused_columns=False, 
    batch_size = 2)

PPO_trainer = PPOTrainer(config = PPO_config, 
                            model = model, 
                            ref_model = model_ref, 
                            tokenizer = tokenizer,
                            dataset = DDict["train"],
                            data_collator = collator
                        )

device = PPO_trainer.accelerator.device

generation_kwargs = {
    "min_length": -1, # don't ignore the EOS token (see above)
    "top_k": 0.0, # no top-k sampling
    "top_p": 1.0, # no nucleus sampling
    "do_sample": True, # yes, we want to sample
    "pad_token_id": tokenizer.pad_token_id, # most decoder models don't have a padding token - use EOS token instead
    "eos_token_id": tokenizer.eos_token_id,
    "max_new_tokens": 750
}

#--train--
for epoch in range(2):
    for batch in tqdm(PPO_trainer.dataloader):
        idList = batch["input_ids_src"]