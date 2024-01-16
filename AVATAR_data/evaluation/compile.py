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
extJavaLibraries = "./AVATAR_data/data_extLibraries/"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)
regex_pattern_normal = re.compile("([0-9]+) error", re.S)
regex_pattern_special = re.compile(", of ([0-9]+) total;", re.S)


def check_python(args):
    programs = []
    errLines = []
    with open(args.input_file, encoding='utf8') as f:
        for line in f:
            programs.append(line.encode().decode("unicode-escape").strip())

    success, error, num_syntax_error, num_indent_error = 0, 0, 0, 0
    for progIndx, program in tqdm(enumerate(programs), total=len(programs)):
        if len(program.strip()) == 0:
            success += 1
            continue
        # find public class name
        public_class_name = 'main'
        if "public class" in program:
            public_class_name = program.split("public class", 1)[1].split()[0]

        subfolderExists = True

        while subfolderExists:
            time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
            folderNm = os.path.join(args.writeDir, time_rand_str)
            
            subfolderExists = os.path.exists(folderNm)
            #print ("exist check:", subfolderExists)
            if not subfolderExists:
                os.makedirs(folderNm, exist_ok = False)
                #print ("folder created:", folderNm)

        program = pyprocessor.detokenize_code(program)
        filename = os.path.join(folderNm, '{}.py'.format(public_class_name))
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)

        command = ["python", "-m", "py_compile", filename]
        p = run(command, stderr=PIPE)
        error_msg = p.stderr.decode("utf-8")
        if len(error_msg) == 0:
            success += 1
        else:
            print (error_msg)
            errLines.append(progIndx + 1)
            error += 1
            if "SyntaxError: " in error_msg:
                num_syntax_error += 1
            elif "IndentationError: " in error_msg:
                num_indent_error += 1

        shutil.rmtree(folderNm, ignore_errors=True)

    print('Success - {}, Errors - {} [Syntax - {}, Indent - {}]'.format(
        success, error, num_syntax_error, num_indent_error)
    )
    totalProgs = len(programs)
    print (f"CompAcc: {success}/{totalProgs} =", (success * 100.0) / totalProgs, "%")
    # print ("Errors in line nos.:", errLines)


def check_java(args):
    global extJavaLibraries
    programs = []
    errLines = []
    numErr_list = []
    with open(args.input_file, encoding='utf8') as f:
        for line in f:
            programs.append(line.encode().decode("unicode-escape").strip())

    success, error, num_errors = 0, 0, 0
    for progIndx, program in tqdm(enumerate(programs), total=len(programs)):
        if len(program.strip()) == 0:
            success += 1
            continue
        # find public class name
        public_class_name = 'main'
        if "public class" in program:
            tokens = program.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]
        elif "public final class" in program:
            tokens = program.split("public final class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]

        subfolderExists = True
        while subfolderExists:
            time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
            folderNm = os.path.join(args.writeDir, time_rand_str)
            subfolderExists = os.path.exists(folderNm)
            if not subfolderExists:
                os.makedirs(folderNm, exist_ok = False)

        program = jprocessor.detokenize_code(program)
        filename = os.path.join(folderNm, '{}.java'.format(public_class_name))
        class_filename = os.path.join(folderNm, '{}.class'.format(public_class_name))
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)

        command = ["javac", "-cp", "{}:{}".format(folderNm, extJavaLibraries), filename]  
        try:
            check_output(command, stderr=STDOUT)
            success += 1
            numErr_list.append(0)
        except CalledProcessError as e:
            errLines.append(progIndx + 1)
            error += 1
            error_content = e.output.decode()  # Get decoded output from subprocess
            print (error_content, flush = True)
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
            numErr_list.append(int(error_count))

        shutil.rmtree(folderNm, ignore_errors=True)

    print('Success - {}, Errors - {} [Total - {}]'.format(success, error, num_errors), flush = True)
    totalProgs = len(programs)
    print (f"CompAcc: {success}/{totalProgs} =", (success * 100.0) / totalProgs, "%", flush = True)
    print ("numErr_list:", sorted(numErr_list), flush = True)
    # print ("Errors in line nos.:", errLines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, help='Source input file')
    parser.add_argument("--language", type=str, help='Language name')
    parser.add_argument("--writeDir", type=str, default = "./", help='Directory where .java, .class, .py files will be written')
    args = parser.parse_args()
    if args.language == 'java':
        check_java(args)
    if args.language == 'python':
        check_python(args)
