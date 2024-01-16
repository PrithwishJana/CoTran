#!/bin/bash

#SBATCH --cpus-per-task=4   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=32000M        # Request the full memory of the node # memory per node, 256000M
#SBATCH --account=def-vganesh
#SBATCH --time=0-3:00      # time (DD-HH:MM)
#SBATCH --output=exptResults/run-%N-%j.out  # %N for node name, %j for jobID

module load cuda
module load python/3.8
module load java/14.0.2
module load mono/6.12.0.122

#To Run: sbatch ./proposed-results/evalScripts.sh

source ~/cotran/bin/activate
export PYTHONPATH="${PYTHONPATH}:${PWD}/AVATAR_data"
#------------------------------------
SOURCE=${2:-java}
TARGET=${3:-python}
MODEL=${4:-CoTranCFSF10}

references=./AVATAR-TC/test.java-python.${TARGET}
predictions=./proposed-results/${MODEL}-${SOURCE}-${TARGET}.${TARGET}
idfile=./AVATAR-TC/test.java-python.id
writeDir='./junk'
#------------------------------------

{
python ./AVATAR_data/evaluation/compile_perDataset.py \
        --input_file ${predictions} \
        --language ${TARGET} \
        --id_file ${idfile} \
        --writeDir ${writeDir}

echo -en '\n'

python ./AVATAR_data/evaluation/evaluator.py \
        --references ${references} \
        --predictions ${predictions} \
        --txt_ref \
        --language ${TARGET}

echo -en '\n'

python ./AVATAR_data/evaluation/CodeBLEU/calc_code_bleu.py \
        --ref ${references} \
        --txt_ref \
        --hyp ${predictions} \
        --lang ${TARGET}

echo -en '\n'

python ./AVATAR_data/evaluation/avgFirstErrPos.py \
        --pathPrediction ${predictions} \
        --DEST_LANG ${TARGET} \
        --writeDirTmp ${writeDir}

echo -en '\n'

python ./AVATAR_data/data_LARGE/runtimeEquivalence_corrections/check_runtimeOutput.py \
        --input_file ${predictions} \
        --id_file ${idfile} \
        --language ${TARGET} \
        --writeDir ${writeDir}
}> ./proposed-results/${MODEL}-${SOURCE}-${TARGET}.results 2>&1