#!/bin/sh

#SBATCH --mem=64000M        # Request the full memory of the node # memory per node, 256000M
#SBATCH --account=def-vganesh
#SBATCH --time=2-00:00      # time (DD-HH:MM)
#SBATCH --ntasks-per-node=4        #same as number of GPUs per node --> 4
#SBATCH --cpus-per-task=6   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --output=symflower_related/run-%N-%j.out  # %N for node name, %j for jobID

module load java/14.0.2
module load mono/6.12.0.122
module load cuda gcc python/3.10 arrow/13.0.0
module load rust/1.70.0

#sbatch symflower_related/runSymflowerForAllTrainJavaCodes.sh

#0..18000 18001..36000 36001..55178
for i in {36001..55178}
do
    FOLDER=$(printf %05d $i)
    cd "symflower_related/tmp/$FOLDER"
    ../../symflower
    cd "../../../"
    echo "$FILE"
done
