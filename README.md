# CoTran: An LLM-based Code Translator using Reinforcement Learning with Feedback from Compiler and Symbolic Execution

## AVATAR-TC Dataset

The paper introduces a new dataset **AVATAR-TC** (built on top of the AVATAR) that has pairs of equivalent whole-programs in Java and Python (a statically- and dynamically-typed language, with different syntactic styles). To the best of our knowledge, AVATAR-TC is the first large-scale dataset of codes in two different languages that has human-written test-cases (TC) for each pair, and guarantees compilability and input-output (IO) equivalence of each pair. 

We use a collection of codes written in Java and Python from five contest websites: Aizu, AtCoder, Codeforces, Google-CodeJam, LeetCode, and two coding platforms: GeeksForGeeks, ProjectEuler.

The codes are parsed into code-specific tokens by javalang and tokenize module. Additionally, we collected test-cases for each of the problems by web-crawling the data sources. Any code that did not match the expected output on supplying the test-case inputs was manually corrected for minor faults, while the ones with major issues were discarded. Output matching is case-insensitive, ignores whitespaces, disregards punctuations (only when they are a minor portion of the output) and takes numeric or floating-point values to a common representation.

The Statistics of the AVATAR-TC benchmark suite is as follows:

<img width="382" alt="Screenshot 2024-01-16 at 2 14 10 AM" src="https://github.com/PrithwishJana/CoTran-Anonymous/assets/26099047/9aae2411-e926-40db-86dd-a4f3ca3bf8f1">

The AVATAR-TC dataset (with all Java-Python code pairs and test-cases) is available at: `./AVATAR-TC/` 

For each of the partition (train/validation/test), there is a file for Java, a file for Python and a file for the problem ID. The folder structure for the code pairs is as follows:

```bash
./AVATAR-TC/
├── test.java-python.id
├── test.java-python.java
├── test.java-python.python
├── train.java-python.id
├── train.java-python.java
├── train.java-python.python
├── valid.java-python.id
├── valid.java-python.java
└── valid.java-python.python
```

Additionally, there are .json files corresponding to each sub-dataset, containing human-written test-cases (TC) i.e. input-output for each Java-Python code pair.

```bash
./AVATAR-TC/
├── io_testcases_aizu.json
├── io_testcases_atcoder.json
├── io_testcases_codeforces.json
├── io_testcases_codejam.json
├── io_testcases_geeksforgeeks.json
├── io_testcases_leetcode.json
└── io_testcases_projecteuler.json
```

## Dependencies
The repository is developed in Python and the following versions were used:
- java/14.0.2
- mono/6.12.0.122
- python/3.10
- arrow/13.0.0
- rust/1.70.0

For all the Python libraries, refer the requirements file provided in the repository. You can also directly setup a virtual environment by the following setup steps.

## Setup
 - For CoTran (baseline), CoTran<sup>+</sup>, CoTran<sup>x</sup>:
   
     ```
     virtualenv --no-download --clear ~/cotran
     source ~/cotran/bin/activate
     pip install -r requirements_cotran.txt
     deactivate
     ```
 - For CoTran+CF, CoTran+CF+SF:
   
     ```
     virtualenv --no-download --clear ~/cotranRL
     source ~/cotranRL/bin/activate
     pip install -r requirements_cotranRL.txt
     deactivate
     ```

## Training \& Evaluating the CoTran (baseline), CoTran<sup>+</sup>, CoTran<sup>x</sup> Models

All the codes for CoTran (baseline) are implemented in Pytorch Lightning and supports multi-GPU as well as multi-node training. During our experimentation, we tried on two compute nodes, each comprising four NVIDIA V100 GPUs with 32GB memory and six CPU cores per GPU. This could fit a batch size of 8x8 = 64 during training.

1. Change the appropriate hyperparameters, number of compute nodes, number of GPUs, batch size, src language, target language, etc. in the shell script `./CoTranBaseline_run_script_TRAIN.sh`.
2. Run `./CoTranBaseline_run_script_TRAIN.sh` for training the CoTran (baseline) Java-to-Python (J2P) and Python-to-Java (P2J) LLMs
3. Run `./CoTranBaseline_run_script_TEST.sh` to evaluate the models, after editing the working directory folder in the script
4. The working directory will contain the best J2P and P2J models, along with the corresponding tokenizer folder.
5. Move the best J2P and P2J models to path `./FINETUNED_MODELS/java2python/bestModel.ckpt` and `./FINETUNED_MODELS/python2java/bestModel.ckpt` respectively
6. Move the respective tokenizers to path `./FINETUNED_MODELS/java2python/tokenizer` and `./FINETUNED_MODELS/python2java/tokenizer` respectively

## Training \& Evaluating the CoTran+CF and CoTran+CF+SF Models
1. For training CoTran + CF (RL only), run `./language_translation_RLonly_CF_runSCRIPT.sh`
2. For training CoTran + CF (RL + SFT interleaved training), run `./language_translation_RLSFT_CF_runSCRIPT.sh`
3. For training CoTran + CF + SF (RL + SFT interleaved training) i.e. back-to-back LLMs, run `./language_translation_RLSFT_CFSF_runSCRIPT.sh`
4. For training CoTran + CF + SF (RL only) just edit `./language_translation_RLSFT_CFSF.py` to comment out the SFT function-call and then, run `./language_translation_RLSFT_CFSF_runSCRIPT.sh`

Each of these will write models in the working directory, and the training can be observed by connecting to WanDB.

## Pre-computed Results
1. For the translation results of J2P and P2J obtained by three human-written transpilers (java2python, TSS Code Converter, py2java), refer folder `./transpilers`. This folder also contains the scripts to execute the transpiler on the AVATAR-TC dataset.
2. For the translation results of J2P and P2J obtained by all the recent state-of-the-art methods, refer folder `./SoTA-results`. It contains the result files and the metric calculation logs for (a) three SoTA LLM-based unsupervised translation tools i.e. TransCoder, TransCoder-DOBF, TransCoder-ST (trained on function pairs from 2.5M open-sourced repositories of the GitHub dataset from Google BigQuery Public Datasets), (b) ChatGPT and, (c) seven LLM-based supervised translation tools i.e. CodeBERT, GraphCodeBERT, CodeGPT, CodeGPT-adapted, PLBART-base, CodeT5-base, PPOCoder
