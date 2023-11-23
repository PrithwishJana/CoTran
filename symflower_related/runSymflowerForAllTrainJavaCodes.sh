#!/bin/sh

#SBATCH --mem=64000M        # Request the full memory of the node # memory per node, 256000M
#SBATCH --account=def-vganesh
#SBATCH --time=0-12:00      # time (DD-HH:MM)

for i in {0..55179}
do
    FOLDER=$(printf %05d $i)
    cd "symflower_related/tmp/$FOLDER"
    ../../symflower
    cd "../../../"
    echo "$FILE"
done
