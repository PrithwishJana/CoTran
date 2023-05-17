from pygments.lexers.jvm import JavaLexer
import re
from os import system as sys2
import os
import codeop
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
import numpy as np
import shutil, time, random, subprocess
from pylint.lint import Run
from pylint.reporters.text import TextReporter
from pathlib import Path
import wandb
import signal
import math, copy
from transformers import RobertaTokenizer, T5ForConditionalGeneration, AutoTokenizer
import compileall
from pygments.token import Token

import sys
from contextlib import contextmanager
from io import StringIO
import cProfile, pstats, io 
import threading

'''
folderCreateMutexLock = threading.Semaphore(value = 1) #threading.Lock()
def initMutexLock():
    this.namefolderCreateMutexLock = threading.Lock
        folderExists = True
        while folderExists:
            time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
            folderNm = os.path.join(tokenizedFileDir, time_rand_str)

            folderCreateMutexLock.acquire() #SEM LOCK
            folderExists = os.path.exists(folderNm)
            #print ("exist check:", folderExists)
            if not folderExists:
                os.makedirs(folderNm, exist_ok = False)
                #print ("folder created:", folderNm)
            folderCreateMutexLock.release() #SEM LOCK
'''

def tokenize_code(code, tokenizer):
    return tokenizer.encode(code, truncation = True, padding = 'max_length', 
                            max_length=512, return_tensors = 'np')

def create_compiler_loss_forBatch(idtokens_allPreds, lang, tokenizer, writeDir, 
                                        BOS_IDX, DEBUG_FLAG, deviceID_str):
    """
    :param idtokens: a 2D np array, where each column represents a different generated code program
                     having list of tokens in id format
    :param lang: type of programming language
    :param tokenizer: tokenizer used by model
    :return: mask
    """    
    extJavaLibraries = "./AVATAR_data/data_extLibraries/"
    root_folder = "./AVATAR_data/third_party"
    jProcessor = JavaProcessor(root_folder=root_folder)
    pyProcessor = PythonProcessor(root_folder=root_folder)

    tokenizedFileDir = os.path.join(writeDir, "tokenizedFiles")
    os.makedirs(tokenizedFileDir, exist_ok=True)

    # initialize compiler mask
    allPreds_shape = idtokens_allPreds.shape
    if DEBUG_FLAG: print ("idtokens_allPreds.shape: ", allPreds_shape)
    try:
        assert np.all(idtokens_allPreds[0,:] == BOS_IDX) == True #all predictions starts with <s>
    except AssertionError:
        print(f"Assertion error with BOS_IDX ({BOS_IDX}) check: some pred. doesn't start with <s>")
        print(idtokens_allPreds[np.where(idtokens_allPreds[0,:] != BOS_IDX)])
    lossAllProgs = np.zeros(allPreds_shape[1], dtype=float) #one scalar loss per program
    if DEBUG_FLAG: print ("lossAllProgs.shape: ", lossAllProgs.shape)

    time_rand_deviceID_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999)) + \
                                "_" + deviceID_str
    folderNm = os.path.join(tokenizedFileDir, time_rand_deviceID_str)
    os.makedirs(folderNm, exist_ok = False)

    idtokens_allPreds_T = np.transpose(idtokens_allPreds)
    decodedfiles = tokenizer.batch_decode(idtokens_allPreds_T, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False)
    assert allPreds_shape[1] == len(decodedfiles)

    if lang == "python":
        py_fileName_list = []
        py_numLines = []

        for progIndx, decodedfile in enumerate(decodedfiles): #for each column
            numLinesInPyProg = decodedfile.count(" NEW_LINE") + 1 #NOTE: NEW_LINE has space in front
            py_numLines.append(numLinesInPyProg)
            decodedfile = pyProcessor.detokenize_code(decodedfile)
            if DEBUG_FLAG: print ("---------------------\n\ndecodedfile:\n" +  decodedfile, "\n")

            fileNm = os.path.join(folderNm, str(progIndx) + ".py")
            py_fileName_list.append(fileNm)
            with open(fileNm, "w") as file1:
                file1.write(decodedfile)

        if DEBUG_FLAG: print ("py_numLines:\n",  py_numLines, "\n")
        errorlog_content_allProgs = subprocess.Popen(["python"] + ["-m", "compileall"] + [folderNm],
                                                        stdout=subprocess.PIPE, text=True).stdout.read()

        if DEBUG_FLAG: print ("---------------------\nerrorlog_content_allProgs:\n" +  errorlog_content_allProgs, "\n")

        for progIndx in range(len(py_fileName_list)): #for each column
            regexStr_to_match = "Compiling.*?" + re.escape(py_fileName_list[progIndx]) +\
                                        "(?:(?!Compiling).|\n)*?line ([0-9]+)"
            regex_pattern = re.compile(regexStr_to_match, re.S)
            error_lineNums = regex_pattern.findall(errorlog_content_allProgs)

            if DEBUG_FLAG: print ("\nerror_lineNums:",  error_lineNums)

            if error_lineNums != None and len(error_lineNums) != 0: 
                error_lineNum = min([int(x) for x in error_lineNums])
                assert error_lineNum != 0
                numLinesInPyProg = py_numLines[progIndx]
                if DEBUG_FLAG: print("Error found at line: {}".format(error_lineNum))   
                lossAllProgs[progIndx] = abs(-math.log((error_lineNum * 1.0 / (numLinesInPyProg + 1))))
                if DEBUG_FLAG: print (str(error_lineNum * 1.0) + " / " + str(numLinesInPyProg + 1)
                                        + " = " + str(abs(-math.log((error_lineNum * 1.0 / (numLinesInPyProg + 1))))))
            else:
                lossAllProgs[progIndx] = abs(-math.log(1.0))
            if DEBUG_FLAG: print ("lossAllProgs[{}]".format(progIndx), lossAllProgs[progIndx])

    elif lang == 'java':
        # set up tokenizers
        javalexer = JavaLexer()

        errMetric_list_perChunk = []
        paths_allProgs = [] #list of lists
        folders_allProgs = [] #list of lists
        tokensLen_allProgs = [] #list of lists 

        for progIndx, oneLineProg in enumerate(decodedfiles):
            decodedfile = jProcessor.detokenize_code(oneLineProg)

            processed_tokens_list = []
            combined_literals = ""
            literal_type = None

            # generate a unique path based on timestamp and random num, to save java code
            folderNm_perProg = os.path.join(folderNm, str(progIndx))
            os.makedirs(folderNm_perProg)
            folders_allProgs.append(folderNm_perProg)

            #replace class name by timestamped name
            timeRandStr = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
            regex_pattern_classNames = re.compile("class\s(\w+?)\s", re.S)
            classNames = regex_pattern_classNames.findall(decodedfile)
            for className in classNames:
                decodedfile = re.sub(r"\s{}\s".format(className), " {}_{} ".format(className, timeRandStr), 
                                    decodedfile)

            # getting public_class_name
            public_class_name_default = 'main_{}'.format(timeRandStr)
            public_class_name = copy.deepcopy(public_class_name_default)
            if "public class" in decodedfile:
                tokens = decodedfile.split("public class", 1)
                if len(tokens) == 2 and len(tokens[1]) > 0:
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
                    
            fileNm = os.path.join(folderNm_perProg, '{}.java'.format(public_class_name))

            try:
                with open(fileNm, 'w') as newfile:
                    newfile.write(strToWrite.rstrip())
            except:
                #for cases like: PermissionError: [Errno 13] Permission denied: '//=.java'
                fileNm = os.path.join(folderNm_perProg, '{}.java'.format(public_class_name_default))
                with open(fileNm, 'w') as newfile:
                    newfile.write(strToWrite.rstrip())

            paths_allProgs.append(fileNm)
            tokensLen_allProgs.append(numTokens)

        # use javac and subprocess call, to get stderr for each code -----------------
        errorlog_content_allProgs = subprocess.Popen(["javac"] + ["-cp", ".:{}".format(extJavaLibraries)] + 
                                                        ["-Xmaxerrs", str(len(paths_allProgs) * 512)] +
                                                        paths_allProgs, 
                                                        stderr = subprocess.PIPE, text = True).stderr.read()

        for folderPath in folders_allProgs:
            shutil.rmtree(folderPath, ignore_errors = True)

        # some assertions to make sure next steps are computed correctly
        assert  len(paths_allProgs) == len(decodedfiles)
        assert len(tokensLen_allProgs) == len(decodedfiles)

        errStrtList = []

        for progIndx in range(len(decodedfiles)): #for each column
            regex_pattern = re.compile(re.escape(paths_allProgs[progIndx]) +\
                                        ":([0-9]+):.error", re.S)
            error_lineNums = regex_pattern.findall(errorlog_content_allProgs)
            if DEBUG_FLAG: print ("\nerror_lineNums:",  error_lineNums)

            if error_lineNums != None and len(error_lineNums) != 0:
                min_error_position = min([int(x) for x in error_lineNums]) #is 1-based, not 0-based
                numLinesInJavaProg = tokensLen_allProgs[progIndx]
                assert min_error_position <= numLinesInJavaProg

                if DEBUG_FLAG: print("Error found at line: {}".format(min_error_position))   
                lossAllProgs[progIndx] = abs(-math.log((min_error_position * 1.0 / (numLinesInJavaProg + 1))))
                if DEBUG_FLAG: print (str(min_error_position * 1.0) + " / " + str(numLinesInJavaProg + 1)
                                        + " = " + str(lossAllProgs[progIndx]))
            else:
                lossAllProgs[progIndx] = abs(-math.log(1.0))
            if DEBUG_FLAG: print ("lossAllProgs[{}]".format(progIndx), lossAllProgs[progIndx])

    else:
        raise NotImplementedError

    shutil.rmtree(folderNm, ignore_errors = True)
    return lossAllProgs




def detokenizeCode_and_append(idtokens, list, tokenizer, removeSpclTokens = None):
    """
    :param idtokens: a list of tokens in id format - represent a generated code program
    :param list: list to store the output programs
    :param tokenizer: tokenizer used by model
    :return: void
    """
    # decode id tokens from the model - generate whole program
    # strip out all switch line characters
    if removeSpclTokens is not None:
        idtokens = np.delete(idtokens, np.where(np.isin(idtokens, removeSpclTokens))[0])
    decoded_file = tokenizer.decode(idtokens, skip_special_tokens = True,
                                            clean_up_tokenization_spaces = False).splitlines()
    mystr = ''.join([line.strip() for line in decoded_file])
    list.append(mystr)





if __name__ == "__main__":

    pr = cProfile.Profile()
    tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-base')

    
    #lang = "python"
    #progList = ['''print ( int ( input ( ) ) // 3 )''',
    #                    '''from heapq import heappush , heappop NEW_LINE class Dijk : NEW_LINE INDEN def __init__ ( self , n ) : NEW_LINE INDENT self . table = [ [ ] for i in range ( n ) ] NEW_LINE self . n = n NEW_LINE DEDENT def add ( self , x , y , f ) : NEW_LINE INDENT self . table [ x ] . append ( ( y , f ) ) NEW_LINE DEDENT def di ( self , s ) : NEW_LINE INDENT inf = 10 ** 20 NEW_LINE self . val = [ inf ] * self . n NEW_LINE self . val [ s ] = 0 NEW_LINE h = [ ] NEW_LINE heappush ( h , ( 0 , s ) ) NEW_LINE while h : NEW_LINE INDENT q , i = heappop ( h ) NEW_LINE if self . val [ i ] < q : NEW_LINE INDENT continue NEW_LINE DEDENT for x , c in self . table [ i ] : NEW_LINE INDENT if self . val [ x ] > self . val [ i ] + c : NEW_LINE INDENT self . val [ x ] = self . val [ i ] + c NEW_LINE heappush ( h , ( self . val [ x ] , x ) ) NEW_LINE DEDENT DEDENT DEDENT DEDENT def dist ( self , s , t ) : NEW_LINE INDENT return self . val [ t ] NEW_LINE DEDENT DEDENT K = int ( input ( ) ) NEW_LINE d = Dijk ( K ) NEW_LINE for i in range ( 1 , K ) : NEW_LINE INDENT d . add ( i , ( i + 1 ) % K , 1 ) NEW_LINE d . add ( i , ( 10 * i ) % K , 0 ) NEW_LINE DEDENT d . di ( 1 ) NEW_LINE print ( d . dist ( 1 , 0 ) + 1 )''',
    #                    '''impor numpy as np NEW_LINE SIZE = 26 NEW_LINE def longSub ( str , k ) : NEW_LINE INDENT freq = np . zeros ( 26 , dtype = np . int ) NEW_LINE start = 0 NEW_LINE maxLen = 0 NEW_LINE n = len ( str ) NEW_LINE for i in range ( 0 , n ) : NEW_LINE INDENT ch = str [ i ] NEW_LINE freq [ ord ( ch ) - ord ( ' a ' ) ] += 1 NEW_LINE if ( freq [ ord ( ch ) - ord ( ' a ' ) ] > k ) : NEW_LINE INDENT if ( maxLen < ( i - start ) ) : NEW_LINE INDENT maxLen = i - start NEW_LINE DEDENT while ( freq [ ord ( ch ) - ord ( ' a ' ) ] > k ) : NEW_LINE INDENT freq [ ord ( str [ start ] ) - ord ( ' a ' ) ] -= 1 NEW_LINE start = start + 1 NEW_LINE DEDENT DEDENT DEDENT if ( maxLen < ( n - start ) ) : NEW_LINE INDENT maxLen = n - start NEW_LINE DEDENT return maxLen ; NEW_LINE DEDENT str = " babcaag " NEW_LINE k = 1 NEW_LINE print ( " Length ▁ = " , longSub ( str , k ) ) NEW_LIN'''
    #]

    lang = "java"
    progList = ['''import java . util . Scanner ;   public class B909 {   public static void main ( String [ ] args ) { Scanner in = new Scanner ( System . in ) ; int N = in . nextInt ( ) ; int answer = ( ( N + 2 ) / 2 ) * ( ( N + 1 ) / 2 ) ; System . out . println ( answer ) ; }   }''',
                    '''class GFG { static int maxN = 20 ; static int maxM = 10 ; static int [ ] [ ] dp = new int [ maxN ] [ maxM ] ; static boolean [ ] [ ] v = new boolean [ maxN ] [ maxM ] ; static int findCnt ( int [ ] arr , int i , int curr , int n , int m ) { if ( i == n ) { if ( curr == 0 ) return 1 ; else return 0 ; } if ( v [ i ] [ curr ] ) return dp [ i ] [ curr ] ; v [ i ] [ curr ] = true ; return dp [ i ] [ curr ] = findCnt ( arr , i + 1 , curr , n , m ) + findCnt ( arr , i + 1 , ( curr + arr [ i ] ) % m , n , m ) ; } public static void main ( String [ ] args ) { int arr [ ] = { 3 , 3 , 3 , 3 } ; int n = arr . length ; int m = 6 ; System . out . println ( findCnt ( arr , 0 , 0 , n , m ) - 1 ) ; } }''',
                    '''import java . io . * ; class GFG { static boolean isBetween ( int a , int b , int c ) { return ( Math . min ( a , b ) <= c && c <= Math . max ( a , b ) ) ; } static boolean canJoin ( int x [ ] , int y [ ] , int i , int j , int k ) { return ( x [ k ] == x [ i ] || x [ k ] == x [ j ] ) && isBetween ( y [ i ] , y [ j ] , y [ k ] ) || ( y [ k ] == y [ i ] || y [ k ] == y [ j ] ) && isBetween ( x [ i ] , x [ j ] , x [ k ] ) ; } static int countLineSegments ( int x [ ] , int y [ ] ) { if ( ( x [ 0 ] == x [ 1 ] && x [ 1 ] == x [ 2 ] ) || ( y [ 0 ] == y [ 1 ] && y [ 1 ] == y [ 2 ] ) ) return 1 ; else if ( canJoin ( x , y , 0 , 1 , 2 ) || canJoin ( x , y , 0 , 2 , 1 ) || canJoin ( x , y , 1 , 2 , 0 ) ) return 2 ; else return 3 ; } public static void main ( String [ ] args ) { int x [ ] = new int [ 3 ] , y [ ] = new int [ 3 ] ; x [ 0 ] = - 1 ; y [ 0 ] = - 1 ; x [ 1 ] = - 1 ; y [ 1 ] = 3 ; x [ 2 ] = 4 ; y [ 2 ] = 3 ; System . out . println ( countLineSegments ( x , y ) ) ; } }'''
    ]
    
    tokMatrix = np.zeros((512, len(progList)))
    for i in range( len(progList)):
        tokList1 = tokenize_code(progList[i], tokenizer).flatten()
        tokMatrix[:, i] = tokList1.transpose()

    pr.enable()
    lossAllProgs = create_compiler_loss_forBatch(tokMatrix, lang, tokenizer, './junk', 
                                        tokenizer.convert_tokens_to_ids(tokenizer.bos_token), True,
                                        'cuda:1')
    pr.disable()
    print ("\nlossAllProgs:", lossAllProgs, "\n")

    '''
    s = io.StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
    '''