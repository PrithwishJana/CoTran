# Attention, Compilation, and Solver-based Symbolic Analysis are All You Need

## Setup

`pip install -r requirements.txt`

## AVATAR-TC Dataset

The AVATAR-TC dataset (with all Java-Python code pairs and test-cases) is available at: `./AVATAR-TC_data/`

## Training \& Evaluating the Models

All codes are implemented in Pytorch Lightning and supports multi-GPU as well as multi-node training. During our experimentation, we tried on two compute nodes, each comprising of four NVIDIA V100 GPUs with 32GB memory and six CPU cores per GPU. This could fit a batch size of $8\times 8 = 64$ for the Stage-I training and $4\times 8 = 32$ for the Stage-II training

1. Change the appropriate hyperparameters, number of compute nodes, number of GPUs, batch size, src language, target language, etc. in the shell scripts.
2. (Stage-I) Run `./run_script_TRAIN.sh` for training the Java-to-Python (J2P) and Python-to-Java (P2J) LLMs
3. Run `run_script_TEST.sh` to evaluate the models, after editing the working directory folder in the script
4. Move the best J2P and P2J models to path `./bestModels/java2py_bestModel.ckpt` and `./bestModels/java2py_bestModel.ckpt` respectively
5. (Stage-II) Run `./run_script_backTrans_TRAIN.sh` for training the back-to-back Java-to-Python-to-Java LLM
6. Run `run_script_TEST.sh` to evaluate the models, after editing the working directory folder in the script
