module load java/14.0.2
module load mono/6.12.0.122
module load cuda gcc python/3.8

virtualenv --no-download --clear ~/cotran

source ~/cotran/bin/activate

pip install --no-index --upgrade pip
pip install --no-index torch
pip install --no-index wandb
pip install transformers
pip install torchinfo==1.6.5
pip install gputil
pip install Pygments==2.12.0
pip install pathvalidate==2.5.2
pip install accelerate==0.13.1 nvidia-ml-py3 pynvml seqeval pandas

pip install sacrebleu==1.2.11 javalang tree_sitter psutil fastBPE

pip install pylint 

pip install antlr4-python3-runtime
pip install openpyxl
pip install styleframe
#https://symflower.com/en/products/symflower-cli/tutorial/cli-java/#installation-tab-manual
./symflower_related/get_symflower.sh
chmod +x ./symflower_related/get_symflower.sh
./symflower_related/symflower --version
pip install pytorch-lightning
pip install torchmetrics

pip uninstall wandb
pip install --no-index wandb==0.13.9
pip uninstall transformers
#pip install transformers==4.26.1
pip install transformers==4.22.0
pip install memory_profiler