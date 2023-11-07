import glob
import linecache
from pathvalidate import ValidationError, validate_filename
from pygments.lexers.c_cpp import CppLexer
from pygments.lexers.jvm import JavaLexer
from pygments.lexers.dotnet import CSharpLexer
from pygments.token import Token
import re, copy
from os import system as sys
import sys as sys2
import os
import codeop
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
import numpy as np
import shutil, time, random, subprocess
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from io import StringIO
from tqdm import tqdm
from pathlib import Path



def computeErrMetric_forPredFile(input_file, lang, writeDir):
    """
    :param input_file: file in one code per line format
    :param lang: type of programming language
    """    
    root_folder = "./AVATAR_data/third_party"
    jProcessor = JavaProcessor(root_folder=root_folder)
    pyProcessor = PythonProcessor(root_folder=root_folder)

    tokenizedFileDir = os.path.join(writeDir, "tokenizedFiles")
    os.makedirs(tokenizedFileDir, exist_ok=True)
        
    programs = []
    with open(input_file, encoding='utf8') as f:
        for line in f:
            programs.append(line.strip())

    #programs = programs[77:78]

    errMetric_list = []

    if lang == "python":
        pylint_params = ["--exit-zero", "--errors-only", '--msg-template', '{line}'] #---FOR PYLINT
        #pylint_params = ["--exit-zero", "--errors-only"] #---FOR PYLINT
        for progIndx, oneLineProgram in tqdm(enumerate(programs), total=len(programs)):
            errMetric = compute_PyError(oneLineProgram, pylint_params, pyProcessor, tokenizedFileDir)
            errMetric_list.append(errMetric)
    elif lang == "java":
        javalexer = JavaLexer()
        chunkSize = 32
        oneLineProgram_chunks = [programs[x:x+chunkSize] for x in range(0, len(programs), chunkSize)]
        for chunkIndx, oneLineProgram_chunk in tqdm(enumerate(oneLineProgram_chunks), total=len(oneLineProgram_chunks)):
            errMetric_list_perChunk = compute_JavaError(oneLineProgram_chunk, javalexer, 
                                                        jProcessor, tokenizedFileDir)
            errMetric_list.extend(errMetric_list_perChunk)
    #print (errMetric_list)
    return sum(errMetric_list) * 1.0 / len(errMetric_list)


def compute_PyError(oneLineProg, pylint_params, pyProcessor, tokenizedFileDir):
    if len(oneLineProg.strip()) == 0:
        return 0.0
    decodedfile = pyProcessor.detokenize_code(oneLineProg)
    error_lineNum = None

    #PYTHON_COMPILER == 'pylint':
    fileNm = os.path.join(tokenizedFileDir, 
                str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999)) + ".py")
    with open(fileNm, "w") as file1:
        file1.write(decodedfile)

    reporter = TextReporter(StringIO())
    Run(pylint_params + [fileNm], reporter=reporter, do_exit=False)
    errorlog_content = reporter.out.getvalue().strip()

    #print (decodedfile)
    #print (errorlog_content)

    Path(fileNm).unlink(missing_ok=True)

    if len(errorlog_content) != 0:
        error_lineNum = int(errorlog_content.split('\n')[1])
        #print("Error found at line: {}".format(error_lineNum)) 

    if error_lineNum is not None:  
        numLinesInPyProg = oneLineProg.count(" NEW_LINE") + 1 #NOTE: NEW_LINE has space in front
        return (error_lineNum * 1.0 / (numLinesInPyProg + 1)) #doing +1, to distinguish from no error
    return 1.0 #when no error

def compute_JavaError(oneLineProg_chunk, javalexer, jProcessor, tokenizedFileDir):
    extJavaLibraries = "./AVATAR_data/data_extLibraries/"
    errMetric_list_perChunk = []
    paths_allProgs = [] #list of lists
    folders_allProgs = [] #list of lists
    tokensLen_allProgs = [] #list of lists 

    for progIndx, oneLineProg in enumerate(oneLineProg_chunk):
        decodedfile = jProcessor.detokenize_code(oneLineProg)

        #print (decodedfile)

        processed_tokens_list = []
        combined_literals = ""
        literal_type = None

        # generate a unique path based on timestamp and random num, to save java code
        timeRandStr = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
        folderNm = os.path.join(tokenizedFileDir, timeRandStr)
        os.makedirs(folderNm)
        folders_allProgs.append(folderNm)

        #replace class name by timestamped name
        regex_pattern_classNames = re.compile("class\s(\w+?)\s", re.S)
        classNames = regex_pattern_classNames.findall(decodedfile)
        #print ("classNames", classNames)
        for className in classNames:
            decodedfile = re.sub(r"\s{}\s".format(className), " {}_{} ".format(className, timeRandStr), 
                                decodedfile)

        # getting public_class_name
        public_class_name_default = 'main_{}'.format(timeRandStr)
        public_class_name = copy.deepcopy(public_class_name_default)
        if "public class" in decodedfile:
            tokens = decodedfile.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                #print (progIndx, tokens)
                public_class_name = tokens[1].split()[0]
        elif "public final class" in decodedfile:
            tokens = decodedfile.split("public final class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]

        # get Java tokens from decodedfile
        tokens = javalexer.get_tokens(decodedfile)

        # combine consecutive literals of Token.Operator, Token.Literal.String, Token.Punctuation
        tokens_list = list(tokens)

        for element in tokens_list:
            #print (element)
            if element[0] in [Token.Operator, Token.Literal.String, Token.Punctuation,
                                Token.Literal.Number.Integer, Token.Name]: #e.g. "double upper = 100d ;"
                if literal_type is None: #turn on, only the first time
                    literal_type = element[0]
                else:
                    literal_type = False
                combined_literals += element[1]
            elif combined_literals != "":
                if literal_type:
                    processed_tokens_list.append((literal_type, combined_literals))
                else:
                    processed_tokens_list.append(("combinedTokType", combined_literals))
                literal_type = None
                combined_literals = ""
                processed_tokens_list.append(element)
            else:
                processed_tokens_list.append(element)

        # create file in one-token-per-line format
        strToWrite = ""
        numTokens = 0

        for value in processed_tokens_list:
            if (value[0] == Token.Text.Whitespace) or (value[0] == Token.Text and len(value[1].strip())==0) \
                    or (value[0] == Token.Error and len(value[1].strip())==0):
                continue
            else:
                strToWrite += '{}\n'.format(value[1])
                numTokens += 1
                
        fileNm = os.path.join(folderNm, '{}.java'.format(public_class_name))
        #print (strToWrite)
        try:
            with open(fileNm, 'w') as newfile:
                newfile.write(strToWrite.rstrip())
        except:
            #for cases like: PermissionError: [Errno 13] Permission denied: '//=.java'
            fileNm = os.path.join(folderNm, '{}.java'.format(public_class_name_default))
            with open(fileNm, 'w') as newfile:
                newfile.write(strToWrite.rstrip())

        paths_allProgs.append(fileNm)
        tokensLen_allProgs.append(numTokens)

    # use javac and subprocess call, to get stderr for each code -----------------

    #errorlog_content_allProgs = subprocess.run(["javac"] + paths_allProgs + 
    #                                            ["-Xmaxerrs", str(len(paths_allProgs) * 500)], 
    #                                            stderr=subprocess.PIPE, text=True).stderr  
    errorlog_content_allProgs = subprocess.Popen(["javac"] + ["-cp", ".:{}".format(extJavaLibraries)] + 
                                                    ["-Xmaxerrs", str(len(paths_allProgs) * 512)] +
                                                    paths_allProgs, 
                                                    stderr=subprocess.PIPE, text=True).stderr.read()

    #print (errorlog_content_allProgs)   

    for folderPath in folders_allProgs:
        shutil.rmtree(folderPath, ignore_errors=True)
    # -----------------

    # some assertions to make sure next steps are computed correctly
    assert  len(paths_allProgs) == len(oneLineProg_chunk)
    assert len(tokensLen_allProgs) == len(oneLineProg_chunk)

    errStrtList = []

    for progIndx in range(len(oneLineProg_chunk)): #for each column
        regex_pattern = re.compile(re.escape(paths_allProgs[progIndx]) +\
                                    ":([0-9]+):.error", re.S)
        error_position = regex_pattern.findall(errorlog_content_allProgs)
        if error_position != None and len(error_position) != 0:
            min_error_position = min([int(x) for x in error_position]) #is 1-based, not 0-based

            #print (min_error_position)

            assert min_error_position <= tokensLen_allProgs[progIndx]
            errMetric_list_perChunk.append(min_error_position * 1.0 / (tokensLen_allProgs[progIndx] + 1))
            #print (min_error_position * 1.0, tokensLen_allProgs[progIndx] + 1) 
            #doing +1, to distinguish from no error
        else:
            errMetric_list_perChunk.append(1.0)

    return errMetric_list_perChunk
