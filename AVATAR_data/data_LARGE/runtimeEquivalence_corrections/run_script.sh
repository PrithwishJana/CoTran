#!/bin/bash
#SBATCH --account=def-vganesh
#SBATCH --time=1-00:00
#SBATCH --cpus-per-task=8

module load cuda
module load python/3.8
module load java/14.0.2
module load mono/6.12.0.122

source ~/cotran/bin/activate
export PYTHONPATH="${PYTHONPATH}:/home/pjana/projects/def-vganesh/pjana/Program-Translation-P1/AVATAR_data"

#python match_runtimeOutput_updtJson.py --input_type train --id_file ../train.java-python.id --writeDir ./junk > out_train.txt 2>&1 

python selectCorrectCodes_formDataSubset.py --input_type train --input_folder ../ORIG_dataSuperset --writeDir ./junk > outALL_train.txt 2>&1 
#python selectCorrectCodes_formDataSubset.py --input_type valid --input_folder ../ORIG_dataSuperset --writeDir ./junk > outALL_valid.txt 2>&1 
#python selectCorrectCodes_formDataSubset.py --input_type test --input_folder ../ORIG_dataSuperset --writeDir ./junk3 > outALL_test.txt 2>&1