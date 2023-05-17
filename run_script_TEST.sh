#!/bin/bash

OUT_FOLD="exptResults/2023-04-29_22-28-09-289514800-6295"  # CHANGE AS PER FOLDER TO TEST ON
echo "Writing output to folder $OUT_FOLD"


for ARGUMENT in "$@"
do
   KEY=$(echo $ARGUMENT | cut -f1 -d=)

   KEY_LENGTH=${#KEY}
   VALUE="${ARGUMENT:$KEY_LENGTH+1}"

   export "$KEY"="$VALUE"
done

# use here your expected variables
echo "cf_mode = $cf_mode" # compiler feedback mode
echo "cf_weight = $cf_weight" # compiler feedback weight
echo "pre_trained = $pre_trained" # pre-train model under use
echo "num_epochs = $num_epochs" # epochs to train the model on
echo "model_mode = $model_mode" # for wandb logs
echo "model_name = $model_name" # for wandb logs
echo "model_tag = $model_tag" # for wandb logs
echo "model_notes = $model_notes" # for wandb logs

module load cuda
module load python/3.8
module load java/14.0.2
module load mono/6.12.0.122

source ~/cotran/bin/activate

#rm *.txt
# rm *.args
#cd ./logs
#rm *.log
#cd ..
#rm -rf ./tokenizedjavafiles

export PYTHONPATH="${PYTHONPATH}:${PWD}/AVATAR_data"

srun python ./language_translation_ParallelTrain.py \
  --num_epochs 0 \
  --src_lang "java" \
  --dest_lang "python" \
  --batch_size 8 \
  --num_nodes 2 \
  --num_gpus_per_node 4 \
  --num_cpu_workers 6 \
  --writeDir "$OUT_FOLD" \
  --model_name "java2py_W_CF0.25_TEST" \
  --model_tag "java2python" \
  --model_notes "for java to python translation with pretrained CodeT5-base model with Compiler feedback, wt 0.25,...only testing" \
  > "$OUT_FOLD/outTEST.txt" 2>&1

echo "Evaluation end"