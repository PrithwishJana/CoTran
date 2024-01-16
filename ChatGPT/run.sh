#!/bin/bash

#SBATCH --cpus-per-task=4   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=32000M        # Request the full memory of the node # memory per node, 256000M
#SBATCH --account=def-vganesh
#SBATCH --time=0-12:00      # time (DD-HH:MM)
#SBATCH --output=exptResults/run-%N-%j.out  # %N for node name, %j for jobID

module load cuda gcc arrow/13.0.0
module load python/3.8
module load java/14.0.2
module load mono/6.12.0.122 
module load rust/1.70.0

#sbatch ./ChatGPT/run.sh

source ~/cotran/bin/activate
export PYTHONPATH="${PYTHONPATH}:${PWD}/AVATAR_data"

python ChatGPT/test_chatgpt.py > "ChatGPT/logJ2P0301.txt" 2>&1

echo "Evaluation end"