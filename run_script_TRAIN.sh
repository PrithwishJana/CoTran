#!/bin/bash

#SBATCH --nodes=2                  #keep 1 for testing
#SBATCH --gpus-per-node=v100l:4    #keep 1 for testing
#SBATCH --ntasks-per-node=4        #same as number of GPUs per node
#SBATCH --cpus-per-task=6   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=128000M        # Request the full memory of the node # memory per node, 256000M
#SBATCH --account=def-vganesh
#SBATCH --time=1-0:00      # time (DD-HH:MM)
#SBATCH --output=exptResults/run-%N-%j.out  # %N for node name, %j for jobID

# Define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H-%M-%S-%N" # current time
}

OUT_FOLD="exptResults/$(timestamp)-$RANDOM"
mkdir -p "$OUT_FOLD"
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

python language_translation_Tokenizer.py \
  --writeDir "$OUT_FOLD"

srun python ./language_translation_ParallelTrain.py \
  --cf_mode 0 \
  --cf_weight 0 \
  --num_epochs 100 \
  --src_lang "python" \
  --dest_lang "java" \
  --batch_size 8 \
  --num_nodes 2 \
  --num_gpus_per_node 4 \
  --num_cpu_workers 6 \
  --writeDir "$OUT_FOLD" \
  --model_name "py2java_W_T5B_WO_CF" \
  --model_tag "python2java" \
  --model_notes "for python to java translation with pretrained CodeT5-base model without Compiler feedback" \
  > "$OUT_FOLD/out.txt" 2>&1

echo "Evaluation end"