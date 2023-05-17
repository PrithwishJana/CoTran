import os
import sys
import re

sys.path.append("..")

import argparse
from tqdm import tqdm
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE
import shutil, time, random


root_folder = "./AVATAR_data/third_party"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)
regex_pattern_normal = re.compile("([0-9]+) error", re.S)
regex_pattern_special = re.compile(", of ([0-9]+) total;", re.S)
f_errPath = None

def check_python(args):
    global f_errPath
    programs = []
    errLines = []
    with open(args.input_file, encoding='utf8') as f:
        for line in f:
            programs.append(line.strip())

    success, error, num_syntax_error, num_indent_error = 0, 0, 0, 0
    for progIndx, programOrig in tqdm(enumerate(programs), total=len(programs)):
        # find public class name
        public_class_name = 'main'
        if "public class" in programOrig:
            public_class_name = programOrig.split("public class", 1)[1].split()[0]

        subfolderExists = True

        while subfolderExists:
            time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
            folderNm = os.path.join(args.writeDir, time_rand_str)
            
            subfolderExists = os.path.exists(folderNm)
            #print ("exist check:", subfolderExists)
            if not subfolderExists:
                os.makedirs(folderNm, exist_ok = False)
                #print ("folder created:", folderNm)

        program = pyprocessor.detokenize_code(programOrig)
        filename = os.path.join(folderNm, '{}.py'.format(public_class_name))
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)

        command = ["python", "-m", "py_compile", filename]
        p = run(command, stderr=PIPE)
        error_msg = p.stderr.decode("utf-8")
        if len(error_msg) == 0:
            success += 1
            f_errPath.write("")
        else:
            errLines.append(progIndx + 1)
            error += 1
            if "SyntaxError: " in error_msg:
                num_syntax_error += 1
            elif "IndentationError: " in error_msg:
                num_indent_error += 1
            f_errPath.write(programOrig)
        f_errPath.write("\n")

        shutil.rmtree(folderNm, ignore_errors=True)

    print('Success - {}, Errors - {} [Syntax - {}, Indent - {}]'.format(
        success, error, num_syntax_error, num_indent_error)
    )
    # print ("Errors in line nos.:", errLines)


def check_java(args):
    global f_errPath
    programs = []
    errLines = []
    with open(args.input_file, encoding='utf8') as f:
        for line in f:
            programs.append(line.strip())

    success, error, num_errors = 0, 0, 0
    for progIndx, programOrig in tqdm(enumerate(programs), total=len(programs)):
        # find public class name
        public_class_name = 'main'
        if "public class" in programOrig:
            tokens = programOrig.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]

        program = jprocessor.detokenize_code(programOrig)
        filename = os.path.join(args.writeDir, '{}.java'.format(public_class_name))
        class_filename = os.path.join(args.writeDir, '{}.class'.format(public_class_name))
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)

        command = ["javac", filename]
        try:
            check_output(command, stderr=STDOUT)
            success += 1
            f_errPath.write("")
        except CalledProcessError as e:
            errLines.append(progIndx + 1)
            error += 1
            error_content = e.output.decode()  # Get decoded output from subprocess
            # First check if there are more than 100 errors, based on result, use regex to extract total error number
            error_number_match = regex_pattern_special.findall(error_content)
            if error_number_match != None and len(error_number_match) != 0:
                error_count = error_number_match[-1]
            else:
                error_number_match = regex_pattern_normal.findall(error_content)
                if error_number_match != None and len(error_number_match) != 0:
                    error_count = error_number_match[-1]
                else:
                    error_count = 1
            num_errors += int(error_count)
            f_errPath.write(programOrig)
        f_errPath.write("\n")

        if os.path.isfile(filename):
            os.remove(filename)
        if os.path.isfile(class_filename):
            os.remove(class_filename)

    print('Success - {}, Errors - {} [Total - {}]'.format(success, error, num_errors))
    # print ("Errors in line nos.:", errLines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, help='Source input file')
    parser.add_argument("--language", type=str, help='Language name')
    parser.add_argument("--writeDir", type=str, default = "./", help='Directory where .java, .class, .py files will be written')
    args = parser.parse_args()
    errPath = os.path.join(os.path.split(args.input_file)[0], "err-" + os.path.split(args.input_file)[1])

    if args.language == 'java':
        f_errPath = open(errPath, "w")
        f_errPath.write("")
        check_java(args)
    if args.language == 'python':
        f_errPath = open(errPath, "w")
        f_errPath.write("")
        check_python(args)
    f_errPath.close()
