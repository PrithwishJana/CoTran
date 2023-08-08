#!/bin/bash
module load cuda
module load python/3.8
module load java/14.0.2
module load mono/6.12.0.122

#To Run: ./SoTA-results/evalScripts.sh

source ~/cotran/bin/activate
export PYTHONPATH="${PYTHONPATH}:${PWD}/AVATAR_data"
#------------------------------------
SOURCE=${2:-python}
TARGET=${3:-java}
MODEL=${4:-codebert}

references=./AVATAR-TC/test.java-python.${TARGET}
predictions=./SoTA-results/${MODEL}-${SOURCE}-${TARGET}.${TARGET}
idfile=./AVATAR-TC/test.java-python.id
writeDir='./junk'
#------------------------------------

{
python ./AVATAR_data/evaluation/compile.py \
        --input_file ${predictions} \
        --language ${TARGET} \
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
}> ./SoTA-results/${MODEL}-${SOURCE}-${TARGET}.results 2>&1