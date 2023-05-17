import os
import sys
import re
import pandas as pd
import time, random
from styleframe import StyleFrame, Styler, utils
import re

#python AVATAR_data/evaluation/compile_errLogToExcel.py --prediction_file ./exptResults/2023-01-27_16-16-30/python_testPredictions_epoch11.txt --references_file ./exptResults/2023-01-27_16-16-30/python_testReferences.txt --language python --writeDir ./junk

#python AVATAR_data/evaluation/compile_errLogToExcel.py --prediction_file ./exptResults/2023-01-27_18-28-18/java_testPredictions_epoch36.txt --references_file ./exptResults/2023-01-27_18-28-18/java_testReferences.txt --language java --writeDir ./junk

sys.path.append("..")

import argparse
from tqdm import tqdm
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE

root_folder = "./AVATAR_data/third_party"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)
regex_pattern_normal = re.compile("([0-9]+) error", re.S)
regex_pattern_special = re.compile(", of ([0-9]+) total;", re.S)

PYTHON_ERROR_CLASSES = [
    'SyntaxError',
    'TypeError',
    'NameError',
    'UnboundLocalError',
    'AttributeError',
    'ZeroDivisionError',
    'IndexError',
    'RecursionError',
    'KeyError',
    'ValueError',
    'OverflowError',
    'IndentationError'
]

JAVA_ERROR_CLASSES = {
    'TypeError': ('list', [
        ('string', 'error: incompatible types:'),
        ('string', 'error: incomparable types:'),
        ('string', 'error: unexpected type'),
        ('string', 'cannot be applied to given types'),
        ('regexp', 'error: .* required, but .* found'),
        ('string', 'error: char cannot be dereferenced'),
        ('string', 'error: int cannot be dereferenced'),
        ('string', 'error: boolean cannot be dereferenced'),
        ('regexp', 'error: .* type not allowed'),
    ]),
    'SyntaxError': ('regexp', 'error: .* expected'),
    'IllegalStartOfExpression': ('string', 'error: illegal start of expression'),
    'ArrayIndexOutOfBoundsException': ('string', 'java.lang.ArrayIndexOutOfBoundsException'),
    'VariableAlreadyDefined': ('regexp', 'error: variable .* is already defined'),
    'NoSuitableMethodFound': ('string', 'error: no suitable method found'),
    'ElseWithoutIf': ('string', "error: 'else' without 'if'"),
    'CantFindSymbol': ('string', 'error: cannot find symbol'),
    'BadOperand': ('string', 'error: bad operand type'),
    'NotAStatement': ('string', 'error: not a statement'),
    'UnclosedStringLiteral': ('string', 'error: unclosed string literal'),
    'UnclosedCharacterLiteral': ('string', 'error: unclosed character literal'),
    'NoReturnStatement': ('string', 'error: missing return statement'),
    'InvalidMethod': ('string', 'error: invalid method declaration; return type required'),
    'StackOverflowError': ('string', 'java.lang.StackOverflowError'),
    'StringIndexOutOfBoundsException': ('string', 'java.lang.StringIndexOutOfBoundsException'),
    'NumberFormatException': ('string', 'java.lang.NumberFormatException'),
    'IllegalArgumentException': ('string', 'java.lang.IllegalArgumentException'),
    'UnreachableStatement': ('string', 'error: unreachable statement'),
    'IntNumberTooLong': ('string', 'error: integer number too large'),
    'NullPointerException': ('string', 'java.lang.NullPointerException'),
    'IndexOutOfBoundsException': ('string', 'java.lang.IndexOutOfBoundsException'),
    'ArithmeticException': ('string', 'java.lang.ArithmeticException'),
    'VariableNotInitialized': ('regexp', 'error: variable .* might not have been initialized'),
    'BreakOutsideSwitchOrLoop': ('string', 'error: break outside switch or loop'),
    'ReachedEndOfFile': ('string', 'error: reached end of file while parsing'),
    'PackageDoesNotExist': ('regexp', 'error: package .* does not exist')
}

def is_match(regex, text):
    pattern = re.compile(regex)
    return pattern.search(text) is not None


def is_match_list(list_of_err_txt, text):
    for v in list_of_err_txt:
        if (v[0] == 'string' and v[1] in text) or \
                (v[0] == 'regexp' and is_match(v[1], text)):
            return True
    return False

def classify_python_errors(errMssg):
    for err in PYTHON_ERROR_CLASSES:
        if err in errMssg:
            return err
    return "Other"

def classify_java_errors(errMssg):
    for k, v in JAVA_ERROR_CLASSES.items():
        if (v[0] == 'string' and v[1] in errMssg) or \
                (v[0] == 'regexp' and is_match(v[1], errMssg)) or \
                (v[0] == 'list' and is_match_list(v[1], errMssg)):
            matched = True
            return k
    return "Other"

def check_python(args):
    global refList, predList, errList, errClass
    programs_pred = []
    programs_ref = []
    errLines = []
    with open(args.references_file, encoding='utf8') as f:
        for line in f:
            programs_ref.append(line.strip())
    with open(args.prediction_file, encoding='utf8') as f:
        for line in f:
            programs_pred.append(line.strip())

    assert len(programs_ref) == len(programs_pred)

    success, error, num_syntax_error, num_indent_error = 0, 0, 0, 0
    for progIndx, program_pred in tqdm(enumerate(programs_pred), total=len(programs_pred)):
        # find public class name
        program_ref = programs_ref[progIndx]
        program_pred_name = 'mainPred_' + str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
        program_pred = pyprocessor.detokenize_code(program_pred)
        program_ref = pyprocessor.detokenize_code(program_ref)

        refList.append(program_ref)
        predList.append(program_pred)

        pred_filename = os.path.join(args.writeDir, '{}.py'.format(program_pred_name))

        with open(pred_filename, 'w', encoding='utf8') as fw:
            fw.write(program_pred)

        command = ["python", "-m", "py_compile", pred_filename]
        p = run(command, stderr=PIPE)
        error_msg = p.stderr.decode("utf-8")
        if len(error_msg) == 0:
            success += 1
            errList.append("")
            errClass.append("")
        else:
            errLines.append(progIndx + 1)
            error += 1
            errList.append(error_msg)
            errClass.append(classify_python_errors(error_msg))
            if "SyntaxError: " in error_msg:
                num_syntax_error += 1
            elif "IndentationError: " in error_msg:
                num_indent_error += 1

        if os.path.isfile(pred_filename):
            os.remove(pred_filename)
        #if progIndx==10: break

    print('Success - {}, Errors - {} [Syntax - {}, Indent - {}]'.format(
        success, error, num_syntax_error, num_indent_error)
    )
    # print ("Errors in line nos.:", errLines)


def check_java(args):
    global refList, predList, errList, errClass
    programs_pred = []
    programs_ref = []
    errLines = []
    with open(args.references_file, encoding='utf8') as f:
        for line in f:
            programs_ref.append(line.strip())
    with open(args.prediction_file, encoding='utf8') as f:
        for line in f:
            programs_pred.append(line.strip())

    assert len(programs_ref) == len(programs_pred)

    success, error, num_errors = 0, 0, 0
    for progIndx, program_pred in tqdm(enumerate(programs_pred), total=len(programs_pred)):
        program_ref = programs_ref[progIndx]

        # find public class name
        public_class_name_pred = 'main'
        if "public class" in program_pred:
            tokens = program_pred.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name_pred = tokens[1].split()[0]

        program_pred = jprocessor.detokenize_code(program_pred)
        program_ref = jprocessor.detokenize_code(program_ref)

        refList.append(program_ref)
        predList.append(program_pred)

        filename = os.path.join(args.writeDir, '{}.java'.format(public_class_name_pred))
        class_filename = os.path.join(args.writeDir, '{}.class'.format(public_class_name_pred))
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program_pred)

        command = ["javac", filename]
        try:
            check_output(command, stderr=STDOUT)
            success += 1
            errList.append("")
            errClass.append("")
        except CalledProcessError as e:
            error += 1
            error_content = e.output.decode()  # Get decoded output from subprocess
            errList.append(error_content)
            errClass.append(classify_java_errors(error_content))

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

        if os.path.isfile(filename):
            os.remove(filename)
        if os.path.isfile(class_filename):
            os.remove(class_filename)

        #if progIndx==10: break

    print('Success - {}, Errors - {} [Total - {}]'.format(success, error, num_errors))
    # print ("Errors in line nos.:", errLines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--references_file", type=str, help='Source input file')
    parser.add_argument("--prediction_file", type=str, help='Source input file')
    parser.add_argument("--language", type=str, help='Language name')
    parser.add_argument("--writeDir", type=str, default = "./", help='Directory where .java, .class, .py files will be written')
    args = parser.parse_args()

    refList = []
    predList = []
    errList = []
    errClass = []

    if args.language == 'java':
        check_java(args)
    if args.language == 'python':
        check_python(args)

    assert len(predList) == len(errList)
    print (len(errClass))

    columns = ['Reference_Code', 'Predicted_Code', 'Error_Stmt_for_Predicted_Code', 'Error_Class']
    df = pd.DataFrame(list(zip(refList, predList, errList, errClass)), columns=columns)

    sf = StyleFrame(df, styler_obj = Styler(horizontal_alignment = utils.horizontal_alignments.left)
                            )
    sf = sf.apply_style_by_indexes(
                                indexes_to_style=[i for i, e in enumerate(errList) if len(e) != 0],
                                styler_obj = Styler(bg_color = '#FFCCCB')
                            )
                            
    sf = sf.apply_style_by_indexes(
                                indexes_to_style=[i for i, e in enumerate(errList) if len(e) == 0],
                                styler_obj = Styler(bg_color = '#90EE90')
                            )
                            
    sf.to_excel("py2java_Errors.xlsx").save()
