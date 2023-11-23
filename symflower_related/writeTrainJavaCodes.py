import os
import sys
import re
import json
import glob
import string

#428 valid, listnode

sys.path.append("..")

import argparse
from tqdm import tqdm
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE
import shutil, time, random
from subprocess import Popen

currPath = "./AVATAR_data/" #"../../../AVATAR_data/"

root_folder = currPath + "third_party"
print (root_folder)
extJavaLibraries = currPath + "data_extLibraries/"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)
regex_pattern_normal = re.compile("([0-9]+) error", re.S)
regex_pattern_special = re.compile(", of ([0-9]+) total;", re.S)

myenv = os.environ.copy()
if os.path.abspath(extJavaLibraries) not in myenv['PYTHONPATH']:
    myenv['PYTHONPATH'] += ":" + os.path.abspath(extJavaLibraries)
    #IMP for python external library, in proj-euler


def runSymflower(programs):
    for oneLineProgIndx, oneLineProg in tqdm(enumerate(programs), total=len(programs)):

        public_class_name = 'Main'
        if "public class" in oneLineProg:
            tokens = oneLineProg.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]
        elif "public final class" in oneLineProg:
            tokens = oneLineProg.split("public final class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]

        program = jprocessor.detokenize_code(oneLineProg)

        folderNm = os.path.join("./symflower_related/tmp", str(oneLineProgIndx).zfill(5))
        os.makedirs(folderNm, exist_ok = False)

        filename = os.path.join(folderNm, '{}.java'.format(public_class_name))
        print (str(oneLineProgIndx).zfill(5), filename)
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)


if __name__ == '__main__':
    trainPath = "./AVATAR-TC/train.java-python.java"
    programs = []
    with open(trainPath, encoding='utf8') as f:
        for line in f:
            programs.append(line.strip())

    runSymflower(programs)
