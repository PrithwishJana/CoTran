import os
import sys
import shutil

sys.path.append("..")

import argparse
from tqdm import tqdm
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE

root_folder = "./AVATAR_data/third_party"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)
f_errPath = None

def check_python(rootPath, errFileNm):
    global writePath
    errFilePath = os.path.join(rootPath, errFileNm)
    programs = []
    progs_lineList = []
    with open(errFilePath, encoding='utf8') as f:
        for lineIndx, line in enumerate(f):
            prog = line.strip()
            if prog != "":
                try:
                    indx = programs.index(prog)
                    progs_lineList[indx].append(lineIndx+1)
                except ValueError:
                    programs.append(prog)
                    progs_lineList.append([lineIndx+1])

    print (len(programs), len(progs_lineList), progs_lineList)

    success, error, num_syntax_error, num_indent_error = 0, 0, 0, 0
    for programOrigIndx, programOrig in tqdm(enumerate(programs), total=len(programs)):
        # find public class name
        public_class_name = 'main'
        if "public class" in programOrig:
            public_class_name = programOrig.split("public class", 1)[1].split()[0]
        lineIndices = progs_lineList[programOrigIndx]
        for lineIndx, line in enumerate(lineIndices):
            lineIndices[lineIndx] = f'{line:05}'
        prefixStr = lineIndices[0] + "_"

        program = pyprocessor.detokenize_code(programOrig)
        filename = '{}{}.py'.format(prefixStr, public_class_name)
        with open(os.path.join(writePath, errFileNm, filename), 'w', encoding='utf8') as fw:
            print ("{} written!".format(os.path.join(writePath, errFileNm, filename)))
            fw.write(program)
        with open(os.path.join(writePath, errFileNm, "lines_" + filename.split('.')[0] + ".txt"), 'w', encoding='utf8') as fw:
            fw.write("_".join(lineIndices))


def check_java(rootPath, errFileNm):
    global writePath
    errFilePath = os.path.join(rootPath, errFileNm)
    programs = []
    progs_lineList = []
    with open(errFilePath, encoding='utf8') as f:
        for lineIndx, line in enumerate(f):
            prog = line.strip()
            if prog != "":
                try:
                    indx = programs.index(prog)
                    progs_lineList[indx].append(lineIndx+1)
                except ValueError:
                    programs.append(prog)
                    progs_lineList.append([lineIndx+1])

    print (len(programs), len(progs_lineList), progs_lineList)

    success, error, num_errors = 0, 0, 0
    for programOrigIndx, programOrig in tqdm(enumerate(programs), total=len(programs)):
        # find public class name
        public_class_name = 'main'
        if "public class" in programOrig:
            tokens = programOrig.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]
        lineIndices = progs_lineList[programOrigIndx]
        for lineIndx, line in enumerate(lineIndices):
            lineIndices[lineIndx] = f'{line:05}'
        prefixStr = lineIndices[0] + "_"

        program = jprocessor.detokenize_code(programOrig)
        filename = '{}{}.java'.format(prefixStr, public_class_name)
        with open(os.path.join(writePath, errFileNm, filename), 'w', encoding='utf8') as fw:
            print ("{} written!".format(os.path.join(writePath, errFileNm, filename)))
            fw.write(program)
        with open(os.path.join(writePath, errFileNm, "lines_" + filename.split('.')[0] + ".txt"), 'w', encoding='utf8') as fw:
            fw.write("_".join(lineIndices))


if __name__ == '__main__':
    rootPath = "/home/pjana/projects/def-vganesh/pjana/AVATAR/data/data/"
    fileList = ["err-valid.java-python.java", "err-test.java-python.java", "err-train.java-python.java", 
                "err-valid.java-python.python", "err-test.java-python.python", "err-train.java-python.python"]

    writePath = os.path.join(rootPath, "err")
    if os.path.exists(writePath):
        shutil.rmtree(writePath)
    os.makedirs(writePath)

    for fileNm in fileList:
        writePath_perFile = os.path.join(writePath, fileNm)
        if not os.path.exists(writePath_perFile):
            os.makedirs(writePath_perFile)
            if fileNm.split('.')[-1] == 'java':
                check_java(rootPath, fileNm)
            elif fileNm.split('.')[-1] == 'python':
                check_python(rootPath, fileNm)
        else:
            print ("Folder {} already exists".format(writePath_perFile))