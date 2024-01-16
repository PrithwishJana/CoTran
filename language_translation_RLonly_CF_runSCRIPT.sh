#!/bin/bash

#SBATCH --nodes=1                  #keep 1 for testing --> 2
#SBATCH --gpus-per-node=v100l:2    #keep 1 for testing --> 4
#SBATCH --ntasks-per-node=2        #same as number of GPUs per node --> 4
#SBATCH --cpus-per-task=6   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=64000M        # Request the full memory of the node # memory per node, 256000M
#SBATCH --account=def-vganesh
#SBATCH --time=2-00:00      # time (DD-HH:MM)
#SBATCH --output=exptResults_RL/run-%N-%j.out  # %N for node name, %j for jobID

#for simple
#salloc --nodes=1 --gpus-per-node=v100l:4 --ntasks=1 --cpus-per-task=6 --mem=64000M --account=def-vganesh --time=0-3:00
#salloc --gres=gpu:v100l:1 --cpus-per-task=6 --mem=32000M --account=def-vganesh --time=0-3:00
#salloc --nodes=1 --gpus-per-node=v100l:4 --ntasks-per-node=4 --cpus-per-task=6 --mem=64000M --account=def-vganesh --time=0-3:00
#salloc --nodes=1 --gpus-per-node=v100l:1 --ntasks-per-node=1 --cpus-per-task=6 --mem=64000M --account=def-vganesh --time=0-1:00
#salloc --nodes=1 --gpus-per-node=v100l:2 --ntasks-per-node=2 --cpus-per-task=6 --mem=64000M --account=def-vganesh --time=0-3:00

# Define a timestamp function
timestamp() {
  date +"%Y-%m-%d_%H-%M-%S-%N" # current time
}

OUT_FOLD="exptResults_RL/$(timestamp)-$RANDOM"
mkdir -p "$OUT_FOLD"
echo "Writing output to folder $OUT_FOLD"

module load java/14.0.2
module load mono/6.12.0.122
module load cuda gcc python/3.10 arrow/13.0.0
module load rust/1.70.0

source ~/cotranRL/bin/activate

export PYTHONPATH="${PYTHONPATH}:${PWD}/AVATAR_data"

#/home/pjana/.cache/huggingface/accelerate/default_config.yaml
#srun --jobid 19216448  --pty watch -n 2 nvidia-smi

#accelerate launch --multi_gpu --num_machines 1  --num_processes 2 language_translation_RL_CF_SF_v2.py \
#python language_translation_RL_CF_SF_v2.py \
#accelerate launch --multi_gpu --num_machines 1  --num_processes 4
accelerate launch --multi_gpu --num_machines 1  --num_processes 2 \
	language_translation_RLonly_CF.py \
  --src_lang "java" \
  --dest_lang "python" \
  --writeDir "$OUT_FOLD" \
  > "$OUT_FOLD/out.txt" 2>&1

#batch 512, 128

echo "Evaluation end"