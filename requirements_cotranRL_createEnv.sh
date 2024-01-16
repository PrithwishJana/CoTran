module load java/14.0.2
module load mono/6.12.0.122
module load cuda gcc python/3.10 arrow/13.0.0
module load rust/1.70.0

virtualenv --no-download --clear ~/cotranRL

source ~/cotranRL/bin/activate

pip install pyarrow==9.0.0
pip install trl
pip install sacrebleu==1.2.11
pip install tree-sitter==0.20.1
pip install javalang==0.13.0
pip install pylint==2.15.5
pip install wandb==0.13.9