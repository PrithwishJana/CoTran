from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
import shutil, time, random, subprocess, os, re, copy
import torch
from pygments.lexers.jvm import JavaLexer
from pygments.token import Token
import sys
import numpy as np
from evaluation.CodeBLEU.calc_code_bleu import get_codebleu

def calculateCompilerReward(codeList, lang, writeDir, deviceID_str, justReturnProgLen = False):
    DEBUG_FLAG = False
    extJavaLibraries = "./AVATAR_data/data_extLibraries/"
    root_folder = "./AVATAR_data/third_party"
    jProcessor = JavaProcessor(root_folder=root_folder)
    pyProcessor = PythonProcessor(root_folder=root_folder)

    tokenizedFileDir = os.path.join(writeDir, "tokenizedFiles")
    os.makedirs(tokenizedFileDir, exist_ok=True)
    time_rand_deviceID_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999)) + \
                                "_" + deviceID_str
    folderNm = os.path.join(tokenizedFileDir, time_rand_deviceID_str)
    os.makedirs(folderNm, exist_ok = False)

    rewardAllProgs = [None for i in range(len(codeList))]
    progLenList = []

    if lang == 'java':
        # set up tokenizers
        javalexer = JavaLexer()

        errMetric_list_perChunk = []
        paths_allProgs = [] #list of lists
        folders_allProgs = [] #list of lists
        tokensLen_allProgs = [] #list of lists 

        for progIndx, oneLineProg in enumerate(codeList):
            decodedfile = jProcessor.detokenize_code(oneLineProg.replace("\n", "\\n"))

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
            try:
                if "public class" in decodedfile:
                    tokens = decodedfile.split("public class", 1)
                    if len(tokens) == 2 and len(tokens[1]) > 0:
                        public_class_name = tokens[1].split()[0]
                elif "public final class" in decodedfile:
                    tokens = decodedfile.split("public final class", 1)
                    if len(tokens) == 2 and len(tokens[1]) > 0:
                        public_class_name = tokens[1].split()[0]
            except:
                pass

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

        progLenList = copy.deepcopy(tokensLen_allProgs)
        if justReturnProgLen:
            return None, progLenList

        # use javac and subprocess call, to get stderr for each code -----------------
        errorlog_content_allProgs = subprocess.Popen(["javac"] + ["-cp", ".:{}".format(extJavaLibraries)] + 
                                                        ["-Xmaxerrs", str(len(paths_allProgs) * 750)] +
                                                        paths_allProgs, 
                                                        stderr = subprocess.PIPE, text = True).stderr.read()

        #print ("errorlog_content_allProgs", errorlog_content_allProgs)
        #print ("paths_allProgs", paths_allProgs)
        for folderPath in folders_allProgs:
            shutil.rmtree(folderPath, ignore_errors = True)

        # some assertions to make sure next steps are computed correctly
        assert  len(paths_allProgs) == len(codeList)
        assert len(tokensLen_allProgs) == len(codeList)

        errStrtList = []

        #print (errorlog_content_allProgs)

        for progIndx in range(len(codeList)): #for each column
            regex_pattern = re.compile(re.escape(paths_allProgs[progIndx]) +\
                                        ":([0-9]+):.error", re.S)
            error_lineNums = regex_pattern.findall(errorlog_content_allProgs)
            if DEBUG_FLAG: print ("\nerror_lineNums:",  error_lineNums)

            if error_lineNums != None and len(error_lineNums) != 0:
                min_error_position = min([int(x) for x in error_lineNums]) #is 1-based, not 0-based
                numLinesInJavaProg = tokensLen_allProgs[progIndx]
                assert min_error_position <= numLinesInJavaProg

                if DEBUG_FLAG: print("Error found at line: {}".format(min_error_position))   
                rewardAllProgs[progIndx] = (min_error_position * 1.0 / (numLinesInJavaProg + 1)) #NOTE!!!
                if DEBUG_FLAG: print (str(min_error_position * 1.0) + " / " + str(numLinesInJavaProg + 1)
                                        + " = " + str(rewardAllProgs[progIndx]))
            else:
                rewardAllProgs[progIndx] = 2.0
            if DEBUG_FLAG: print ("rewardAllProgs[{}]".format(progIndx), rewardAllProgs[progIndx])

    elif lang == "python":
        py_fileName_list = []
        py_numLines = []

        for progIndx, decodedfile in enumerate(codeList): #for each column
            if DEBUG_FLAG: print (progIndx, "\n")
            numLinesInPyProg = decodedfile.count(" NEW_LINE") + 1 #NOTE: NEW_LINE has space in front
            py_numLines.append(numLinesInPyProg)
            decodedfile = pyProcessor.detokenize_code(decodedfile.replace("\n", "\\n"))
            if DEBUG_FLAG: print ("---------------------\n\ndecodedfile:\n" +  decodedfile, "\n")

            fileNm = os.path.join(folderNm, str(progIndx) + ".py")
            py_fileName_list.append(fileNm)
            with open(fileNm, "w") as file1:
                file1.write(decodedfile)

        progLenList = copy.deepcopy(py_numLines)
        if justReturnProgLen:
            return None, progLenList

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
                rewardAllProgs[progIndx] = (error_lineNum * 1.0 / (numLinesInPyProg + 1)) #NOTE!!!
                if DEBUG_FLAG: print (str(error_lineNum * 1.0) + " / " + str(numLinesInPyProg + 1)
                                        + " = " + str((error_lineNum * 1.0 / (numLinesInPyProg + 1))))
            else:
                rewardAllProgs[progIndx] = 2.0
            if DEBUG_FLAG: print ("rewardAllProgs[{}]".format(progIndx), rewardAllProgs[progIndx])

    else:
        raise NotImplementedError

    shutil.rmtree(folderNm, ignore_errors = True)
    #rewardAllProgs = [(((x - 0) / (0.8 - 0)) - 1.0) if x < 0.8 else (((x - 0.8) / (1.0 - 0.8)) + 0.0) for x in rewardAllProgs]
    rewardAllProgs = [torch.tensor(float(x)) for x in rewardAllProgs]
    return rewardAllProgs, progLenList

def gaussian(x, mu, sig):
    #1. /( np.sqrt(2. * np.pi) * sig) * 
    return np.exp(-np.power((x - mu) / sig, 2.) / 2)

def calculateCompilerRewardModified(hypCodeList, refCodeList, lang, writeDir, deviceID_str):
    linear_rewardAllProgs, hypCodeLenList = calculateCompilerReward(hypCodeList, lang, writeDir, deviceID_str)
    _, refCodeLenList = calculateCompilerReward(refCodeList, lang, writeDir, deviceID_str)
    hypCodeLenNP, refCodeLenNP = np.array(hypCodeLenList), np.array(refCodeLenList)
    linear_rewardAllProgs_NP = np.array(linear_rewardAllProgs) #mapping from 0 to 2

    sig = refCodeLenNP / 4
    lenDiffMultiplier = gaussian(hypCodeLenNP, refCodeLenNP, sig)
    #print ("lenDiffMultiplier, linear_rewardAllProgs", lenDiffMultiplier, linear_rewardAllProgs)
    rewardAllProgs = (linear_rewardAllProgs * lenDiffMultiplier) - 1
    rewardAllProgs = [torch.tensor(float(x)) for x in rewardAllProgs]
    return rewardAllProgs #mapping from -1 to 1




def calcCodeBLEUreward(hypCodeList, refCodeList, lang, writeDir, deviceID_str):
    assert len(hypCodeList) == len(refCodeList)
    codeBLEURewardAllProgs = []
    time_rand_deviceID_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999)) + \
                                "_" + deviceID_str
    folderNm = os.path.join(writeDir, time_rand_deviceID_str)
    os.makedirs(folderNm, exist_ok = False)

    for i in range(len(hypCodeList)):
        predSavePath = os.path.join(folderNm, f"CBRewardPred_{i}.{lang}")
        with open(predSavePath, 'w', encoding = 'utf-8') as f:
            line = hypCodeList[i].encode("unicode_escape").decode("utf-8")
            f.write(f"{line}\n")

        refSavePath = os.path.join(folderNm, f"CBRewardRef_{i}.{lang}")
        with open(refSavePath, 'w', encoding = 'utf-8') as f:
            line = refCodeList[i].encode("unicode_escape").decode("utf-8")
            f.write(f"{line}\n")

        cb = get_codebleu(refSavePath, predSavePath, lang, '0.25,0.25,0.25,0.25', True)
        codeBLEURewardAllProgs.append(cb)

    shutil.rmtree(folderNm, ignore_errors = True)
    codeBLEURewardAllProgs = [torch.tensor(float(x)) for x in codeBLEURewardAllProgs]
    assert len(codeBLEURewardAllProgs) == len(hypCodeList)

    return codeBLEURewardAllProgs

def calcCodeBLEUrewardWithMinLenPenalty(hypCodeList, refCodeList, lang, writeDir, deviceID_str):
    codeBLEURewardAllProgs = calcCodeBLEUreward(hypCodeList, refCodeList, lang, writeDir, deviceID_str)
    codeBLEURewardAllProgs = [x * 20 for x in codeBLEURewardAllProgs]
    strLenList = [len(x.split()) for x in hypCodeList]
    belowMinLen_BoolList = [x < 50 for x in strLenList]
    print ("strLenList", strLenList)
    print ("belowMinLen_BoolList", belowMinLen_BoolList)
    codeBLEURewardAllProgsClip = [torch.tensor(-10.0) if belowMinLen_BoolList[i]
                                     else x 
                                     for i, x in enumerate(codeBLEURewardAllProgs)]
    return codeBLEURewardAllProgsClip

def calculateRuntimeReward(codeList_pred, lang, probIDs, writeDir, deviceID_str):
    DEBUG_FLAG = False
    extJavaLibraries = "./AVATAR_data/data_extLibraries/"
    root_folder = "./AVATAR_data/third_party"
    jProcessor = JavaProcessor(root_folder=root_folder)
    pyProcessor = PythonProcessor(root_folder=root_folder)

    if DEBUG_FLAG: print (len(codeList_pred), len(probIDs))
    assert len(codeList_pred) == len(probIDs)
    runtimeRewardAllProgs = []
    time_rand_deviceID_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999)) + \
                                "_" + deviceID_str
    folderNm = os.path.join(writeDir, time_rand_deviceID_str)
    os.makedirs(folderNm, exist_ok = False)

    predSavePath = os.path.join(folderNm, f"RunRewardPred.{lang}")
    with open(predSavePath, 'w', encoding = 'utf-8') as f:
        for line in codeList_pred:
            #if (lang == "python"):
            #    line = " ".join(pyProcessor.tokenize_code(pyProcessor.detokenize_code(line)))
            #elif (lang == "java"):
            #    line = " ".join(jProcessor.tokenize_code(jProcessor.detokenize_code(line)))
            #line = line.replace("\\n", "▁").replace("\n", "▁")
            line = line.encode("unicode_escape").decode("utf-8")
            f.write(f"{line}\n")

    idSavePath = os.path.join(folderNm, f"RunRewardID-{lang}.txt")
    with open(idSavePath, 'w', encoding = 'utf-8') as f:
        for line in probIDs:
            f.write(f"{line}\n")

    log = subprocess.Popen(["python"] + 
                            ["./AVATAR_data/data_LARGE/runtimeEquivalence_corrections/check_runtimeOutput.py"] +
                            ["--input_file", predSavePath] +
                            ["--id_file", idSavePath] +
                            ["--language", lang] +
                            ["--writeDir", folderNm], 
                                stdout = subprocess.PIPE, text = True).stdout.read()

    if DEBUG_FLAG: print ("log:", log)
    print ("log:", log)
    matchedUnmatchedStats = re.findall(r"(MATCHED!!.:D|DIDN'T.MATCH!!.:\()", log)
    for mu in matchedUnmatchedStats:
        if (mu == "MATCHED!! :D"):
            runtimeRewardAllProgs.append(1.0)
        else:
            runtimeRewardAllProgs.append(0.0)
    if DEBUG_FLAG: print ("runtimeRewardAllProgs:", runtimeRewardAllProgs)

    shutil.rmtree(folderNm, ignore_errors = True)
    runtimeRewardAllProgs = [torch.tensor(float(x)) for x in runtimeRewardAllProgs]
    assert len(runtimeRewardAllProgs) == len(codeList_pred)
    return runtimeRewardAllProgs


#================== MAIN ======================
if __name__ == '__main__':
    javaCodeList = ['import java . io . BufferedReader ; import java . io . IOException ; import java . io . InputStreamReader ; import java . util . Arrays ; public class Main { public static void main ( String [ ] args ) throws NumberFormatException , IOException { BufferedReader br = new BufferedReader ( new InputStreamReader ( System . in ) ) ; PrimeNumberGenerator pg = new PrimeNumberGenerator ( ) ; while ( true ) { int n = Integer . parseInt ( br . readLine ( ) ) ; if ( n == 0 ) { break ; } if ( pg . isPrime ( n ) ) { System . out . println ( 0 ) ; continue ; } int begin = - 1 ; int end = - 1 ; for ( int i = n - 1 ; i >= 0 ; i -- ) { if ( pg . isPrime ( i ) ) { begin = i ; break ; } } for ( int i = n + 1 ; i < 2000000 ; i ++ ) { if ( pg . isPrime ( i ) ) { end = i ; break ; } } System . out . println ( end - begin ) ; } } } class PrimeNumberGenerator { private final int N = 2000000 ; private boolean [ ] isPrime = new boolean [ N + 1 ] ; public PrimeNumberGenerator ( ) { Arrays . fill ( isPrime , true ) ; isPrime [ 0 ] = false ; isPrime [ 1 ] = false ; int limit = ( int ) Math . sqrt ( N ) ; for ( int i = 2 ; i <= limit ; i ++ ) { if ( isPrime [ i ] == false ) { continue ; } for ( int j = i * 2 ; j <= N ; j += i ) { isPrime [ j ] = false ; } } } public boolean isPrime ( int index ) { return isPrime [ index ] ; } }',
    "public class GFG { static char MAX_CHAR = 26 ; static void countFreq ( String str , int freq [ ] , int len ) { for ( int i = 0 ; i < len ; i ++ ) { freq [ str . charAt ( i ) - ' a ' ] ++ ; } } static boolean canMakePalindrome ( int freq [ ] , int len ) { int count_odd = 0 ; for ( int i = 0 ; i < MAX_CHAR ; i ++ ) { if ( freq [ i ] % 2 != 0 ) { count_odd ++ ; } } if ( len % 2 == 0 ) { if ( count_odd > 0 ) { return false ; } else { return true ; } } if ( count_odd != 1 ) { return false ; } return true ; } static String findOddAndRemoveItsFreq ( int freq [ ] ) { String odd_str = \" \" ; for ( int i = 0 ; i < MAX_CHAR ; i ++ ) { if ( freq [ i ] % 2 != 0 ) { freq [ i ] -- ; odd_str = odd_str + ( char ) ( i + ' a ' ) ; return odd_str ; } } return odd_str ; } static String findPalindromicString ( String str ) { int len = str . length ( ) ; int freq [ ] = new int [ MAX_CHAR ] ; countFreq ( str , freq , len ) ; if ( ! canMakePalindrome ( freq , len ) ) { return \" No ▁ Palindromic ▁ String \" ; } String odd_str = findOddAndRemoveItsFreq ( freq ) ; String front_str = \" \" , rear_str = \" ▁ \" ; for ( int i = 0 ; i < MAX_CHAR ; i ++ ) { String temp = \" \" ; if ( freq [ i ] != 0 ) { char ch = ( char ) ( i + ' a ' ) ; for ( int j = 1 ; j <= freq [ i ] / 2 ; j ++ ) { temp = temp + ch ; } front_str = front_str + temp ; rear_str = temp + rear_str ; } } return ( front_str + odd_str + rear_str ) ; } public static void main ( String [ ] args ) { String str = \" malayalam \" ; System . out . println ( findPalindromicString ( str ) ) ; } }",
    'import java . awt . geom . Line2D ; import java . util . * ; public class Main { Scanner in = new Scanner ( System . in ) ; public static void main ( String [ ] args ) { new Main ( ) ; } public Main ( ) { int q = in . nextInt ( ) ; for ( int i = 0 ; i < q ; i ++ ) new CGL_2B ( ) . doIt ( ) ; } class CGL_2B { double segSegDist ( Line2D l1 , Line2D l2 ) { return l1 . intersectsLine ( l2 ) ? 0 : Math . min ( Math . min ( l1 . ptSegDist ( l2 . getP1 ( ) ) , l1 . ptSegDist ( l2 . getP2 ( ) ) ) , Math . min ( l2 . ptSegDist ( l1 . getP1 ( ) ) , l2 . ptSegDist ( l1 . getP2 ( ) ) ) ) ; } void doIt ( ) { Line2D l1 = new Line2D . Double ( in . nextDouble ( ) , in . nextDouble ( ) , in . nextDouble ( ) , in . nextDouble ( ) ) ; ; Line2D l2 = new Line2D . Double ( in . nextDouble ( ) , in . nextDouble ( ) , in . nextDouble ( ) , in . nextDouble ( ) ) ; ; System . out . printf ( " % .10f \n " , segSegDist ( l1 , l2 ) ) ; } } }',
    "public class GFG { static int count9s ( char number [ ] ) { int n = number . length ; int d [ ] = new int [ 9 ] ; d [ 0 ] = 1 ; int result = 0 ; int mod_sum = 0 , continuous_zero = 0 ; for ( int i = 0 ; i < n ; i ++ ) { if ( ( number [ i ] - '0' ) == 0 ) { continuous_zero ++ ; } else { continuous_zero = 0 ; } mod_sum += ( number [ i ] - '0' ) ; mod_sum %= 9 ; result += d [ mod_sum ] ; d [ mod_sum ] ++ ; result -= continuous_zero ; } return result ; } public static void main ( String [ ] args ) { System . out . println ( count9s ( \"01809\" . toCharArray ( ) ) ) ; System . out . println ( count9s ( \"1809\" . toCharArray ( ) ) ) ; System . out . println ( count9s ( \"4189\" . toCharArray ( ) ) ) ; } }",
    'import java . io . * ; public class GFG { static int fastPow ( int N , int K ) { if ( K == 0 ) return 1 ; int temp = fastPow ( N , K / 2 ) ; if ( K % 2 == 0 ) return temp * temp ; else return N * temp * temp ; } static int countWays ( int N , int K ) { return K * fastPow ( K - 1 , N - 1 ) ; } public static void main ( String [ ] args ) { int N = 3 , K = 3 ; System . out . println ( countWays ( N , K ) ) ; } }',
    'import java . util . Scanner ; public class Main { public static void main ( String [ ] args ) { Scanner sc = new Scanner ( System . in ) ; int [ ] [ ] s = { { 0 , 1 , 1 , 1 , 1 , 1 , 1 } , { 0 , 0 , 0 , 0 , 1 , 1 , 0 } , { 1 , 0 , 1 , 1 , 0 , 1 , 1 } , { 1 , 0 , 0 , 1 , 1 , 1 , 1 } , { 1 , 1 , 0 , 0 , 1 , 1 , 0 } , { 1 , 1 , 0 , 1 , 1 , 0 , 1 } , { 1 , 1 , 1 , 1 , 1 , 0 , 1 } , { 0 , 1 , 0 , 0 , 1 , 1 , 1 } , { 1 , 1 , 1 , 1 , 1 , 1 , 1 } , { 1 , 1 , 0 , 1 , 1 , 1 , 1 } } ; for ( ; ; ) { int n = sc . nextInt ( ) ; int [ ] a = new int [ 7 ] ; if ( n == - 1 ) { break ; } while ( n -- > 0 ) { int m = sc . nextInt ( ) ; for ( int i = 0 ; i < 7 ; i ++ ) { System . out . print ( ( a [ i ] ^ s [ m ] [ i ] ) + ( i == 6 ? " \n " : " " ) ) ; } a = s [ m ] . clone ( ) ; } } } }',
    'import java . util . * ; public class GFG { static final int MAX = 10000 ; static Vector < Integer > arr = new Vector < Integer > ( ) ; static void SieveOfEratosthenes ( ) { boolean [ ] prime = new boolean [ MAX ] ; for ( int i = 0 ; i < MAX ; i ++ ) prime [ i ] = true ; for ( int p = 2 ; p * p < MAX ; p ++ ) { if ( prime [ p ] == true ) { for ( int i = p * 2 ; i < MAX ; i += p ) prime [ i ] = false ; } } for ( int p = 2 ; p < MAX ; p ++ ) if ( prime [ p ] ) arr . add ( p ) ; } static boolean isEuclid ( long n ) { long product = 1 ; int i = 0 ; while ( product < n ) { product = product * arr . get ( i ) ; if ( product + 1 == n ) return true ; i ++ ; } return false ; } public static void main ( String [ ] args ) { SieveOfEratosthenes ( ) ; long n = 31 ; if ( isEuclid ( n ) ) System . out . println ( " YES " ) ; else System . out . println ( " NO " ) ; n = 42 ; if ( isEuclid ( n ) ) System . out . println ( " YES " ) ; else System . out . println ( " NO " ) ; } }',
    'import java . util . * ; public class GFG { static final int MAX = 1000000 ; static Vector < Integer > arr = new Vector < Integer > ( ) ; static boolean [ ] prime = new boolean [ MAX ] ; static void SieveOfEratosthenes ( ) { for ( int i = 0 ; i < MAX ; i ++ ) prime [ i ] = true ; for ( int p = 2 ; p * p < MAX ; p ++ ) { if ( prime [ p ] == true ) { for ( int i = p * 2 ; i < MAX ; i += p ) prime [ i ] = false ; } } for ( int p = 2 ; p < MAX ; p ++ ) if ( prime [ p ] ) arr . add ( p ) ; } static boolean isPrimorialPrime ( int n ) { if ( ! prime [ n ] ) return false ; long product = 1 ; int i = 0 ; while ( product < n ) { product = product * arr . get ( i ) ; if ( product + 1 == n || product - 1 == n ) return true ; i ++ ; } return false ; } public static void main ( String [ ] args ) { SieveOfEratosthenes ( ) ; int n = 31 ; if ( isPrimorialPrime ( n ) ) System . out . println ( " YES " ) ; else System . out . println ( " NO " ) ; } }'
    ]
    pyCodeList = ['import math NEW_LINE def sieve_of_erastosthenes ( num ) : NEW_LINE INDENT input_list = [ False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range ( num ) ] NEW_LINE input_list [ 0 ] = input_list [ 1 ] = False NEW_LINE input_list [ 2 ] = input_list [ 3 ] = input_list [ 5 ] = True NEW_LINE sqrt = math . sqrt ( num ) NEW_LINE for serial in range ( 3 , num , 2 ) : NEW_LINE INDENT if serial >= sqrt : NEW_LINE INDENT return input_list NEW_LINE DEDENT for s in range ( serial ** 2 , num , serial ) : NEW_LINE INDENT input_list [ s ] = False NEW_LINE DEDENT DEDENT DEDENT primeTable = sieve_of_erastosthenes ( 13 * ( 10 ** 5 ) ) NEW_LINE while True : NEW_LINE INDENT k = int ( input ( ) ) NEW_LINE if k == 0 : NEW_LINE INDENT break NEW_LINE DEDENT if primeTable [ k ] : NEW_LINE INDENT print ( 0 ) NEW_LINE DEDENT else : NEW_LINE INDENT i = k NEW_LINE while primeTable [ i ] is False : i += 1 NEW_LINE j = i - 1 NEW_LINE while primeTable [ j ] is False : j -= 1 NEW_LINE print ( i - j ) NEW_LINE DEDENT DEDENT',
    "MAX_CHAR = 26 ; NEW_LINE def countFreq ( str1 , freq , len1 ) : NEW_LINE INDENT for i in range ( len1 ) : NEW_LINE INDENT freq [ ord ( str1 [ i ] ) - ord ( ' a ' ) ] += 1 ; NEW_LINE DEDENT DEDENT def canMakePalindrome ( freq , len1 ) : NEW_LINE INDENT count_odd = 0 ; NEW_LINE for i in range ( MAX_CHAR ) : NEW_LINE INDENT if ( freq [ i ] % 2 != 0 ) : NEW_LINE INDENT count_odd += 1 ; NEW_LINE DEDENT DEDENT if ( len1 % 2 == 0 ) : NEW_LINE INDENT if ( count_odd > 0 ) : NEW_LINE INDENT return False ; NEW_LINE DEDENT else : NEW_LINE INDENT return True ; NEW_LINE DEDENT DEDENT if ( count_odd != 1 ) : NEW_LINE INDENT return False ; NEW_LINE DEDENT return True ; NEW_LINE DEDENT def findOddAndRemoveItsFreq ( freq ) : NEW_LINE INDENT odd_str = ' ' ; NEW_LINE for i in range ( MAX_CHAR ) : NEW_LINE INDENT if ( freq [ i ] % 2 != 0 ) : NEW_LINE INDENT freq [ i ] -= 1 ; NEW_LINE odd_str += chr ( i + ord ( ' a ' ) ) ; NEW_LINE return odd_str ; NEW_LINE DEDENT DEDENT return odd_str ; NEW_LINE DEDENT def findPalindromicString ( str1 ) : NEW_LINE INDENT len1 = len ( str1 ) ; NEW_LINE freq = [ 0 ] * MAX_CHAR ; NEW_LINE countFreq ( str1 , freq , len1 ) ; NEW_LINE if ( canMakePalindrome ( freq , len1 ) == False ) : NEW_LINE INDENT return ' No ▁ Palindromic ▁ String ' ; NEW_LINE DEDENT odd_str = findOddAndRemoveItsFreq ( freq ) ; NEW_LINE front_str = ' ' ; NEW_LINE rear_str = ' ▁ ' ; NEW_LINE for i in range ( MAX_CHAR ) : NEW_LINE INDENT temp = ' ' ; NEW_LINE if ( freq [ i ] != 0 ) : NEW_LINE INDENT ch = chr ( i + ord ( ' a ' ) ) ; NEW_LINE for j in range ( 1 , int ( freq [ i ] / 2 ) + 1 ) : NEW_LINE INDENT temp += ch ; NEW_LINE DEDENT front_str += temp ; NEW_LINE rear_str = temp + rear_str ; NEW_LINE DEDENT DEDENT return ( front_str + odd_str + rear_str ) ; NEW_LINE DEDENT str1 = ' malayalam ' ; NEW_LINE print ( findPalindromicString ( str1 ) ) ; NEW_LINE",
    'import math NEW_LINE def cross ( a , b ) : NEW_LINE INDENT return a . real * b . imag - a . imag * b . real NEW_LINE DEDENT def dot ( a , b ) : NEW_LINE INDENT return a . real * b . real + a . imag * b . imag NEW_LINE DEDENT def norm2 ( a , b ) : NEW_LINE INDENT return ( b . real - a . real ) ** 2 + ( b . imag - a . imag ) ** 2 NEW_LINE DEDENT def is_intersect ( p0 , p1 , p2 , p3 ) : NEW_LINE INDENT ta = cross ( p1 - p0 , p2 - p0 ) NEW_LINE tb = cross ( p1 - p0 , p3 - p0 ) NEW_LINE tc = cross ( p3 - p2 , p0 - p2 ) NEW_LINE td = cross ( p3 - p2 , p1 - p2 ) NEW_LINE if ta * tb < 0 and tc * td < 0 : NEW_LINE INDENT return True NEW_LINE DEDENT else : NEW_LINE INDENT return False NEW_LINE DEDENT DEDENT def distance_option ( p0 , p1 , p2 ) : NEW_LINE INDENT nn = norm2 ( p0 , p1 ) NEW_LINE if 0 <= dot ( p1 - p0 , p2 - p0 ) <= nn : NEW_LINE INDENT return abs ( cross ( p1 - p0 , p2 - p0 ) ) / math . sqrt ( nn ) NEW_LINE DEDENT else : NEW_LINE INDENT return math . sqrt ( min ( norm2 ( p0 , p2 ) , norm2 ( p1 , p2 ) ) ) NEW_LINE DEDENT DEDENT def distance ( p0 , p1 , p2 , p3 ) : NEW_LINE INDENT if is_intersect ( p0 , p1 , p2 , p3 ) : NEW_LINE INDENT return 0 NEW_LINE DEDENT else : NEW_LINE INDENT return min ( distance_option ( p0 , p1 , p2 ) , distance_option ( p0 , p1 , p3 ) , distance_option ( p2 , p3 , p0 ) , distance_option ( p2 , p3 , p1 ) ) NEW_LINE DEDENT DEDENT q = int ( input ( ) ) NEW_LINE for _ in [ 0 ] * q : NEW_LINE INDENT x_y = map ( int , input ( ) . split ( ) ) NEW_LINE p0 , p1 , p2 , p3 = [ x + y * 1j for x , y in zip ( * [ x_y ] * 2 ) ] NEW_LINE print ( " { : . 10f } " . format ( distance ( p0 , p1 , p2 , p3 ) ) ) NEW_LINE DEDENT',
    "def count9s ( number ) : NEW_LINE INDENT n = len ( number ) NEW_LINE d = [ 0 for i in range ( 9 ) ] NEW_LINE d [ 0 ] = 1 NEW_LINE result = 0 NEW_LINE mod_sum = 0 NEW_LINE continuous_zero = 0 NEW_LINE for i in range ( n ) : NEW_LINE INDENT if ( ord ( number [ i ] ) - ord ( '0' ) == 0 ) : NEW_LINE INDENT continuous_zero += 1 NEW_LINE DEDENT else : NEW_LINE INDENT continuous_zero = 0 NEW_LINE DEDENT mod_sum += ord ( number [ i ] ) - ord ( '0' ) NEW_LINE mod_sum %= 9 NEW_LINE result += d [ mod_sum ] NEW_LINE d [ mod_sum ] += 1 NEW_LINE result -= continuous_zero NEW_LINE DEDENT return result NEW_LINE DEDENT if __name__ == ' _ _ main _ _ ' : NEW_LINE INDENT print ( count9s ( '01809' ) ) NEW_LINE print ( count9s ( '1809' ) ) NEW_LINE print ( count9s ( '4189' ) ) NEW_LINE DEDENT",
    'def fastPow ( N , K ) : NEW_LINE INDENT if ( K == 0 ) : NEW_LINE INDENT return 1 ; NEW_LINE DEDENT temp = fastPow ( N , int ( K / 2 ) ) ; NEW_LINE if ( K % 2 == 0 ) : NEW_LINE INDENT return temp * temp ; NEW_LINE DEDENT else : NEW_LINE INDENT return N * temp * temp ; NEW_LINE DEDENT DEDENT def countWays ( N , K ) : NEW_LINE INDENT return K * fastPow ( K - 1 , N - 1 ) ; NEW_LINE DEDENT N = 3 ; NEW_LINE K = 3 ; NEW_LINE print ( countWays ( N , K ) ) ; NEW_LINE',
    "NUM = ( 0b0111111 , 0b0000110 , 0b1011011 , 0b1001111 , 0b1100110 , 0b1101101 , 0b1111101 , 0b0100111 , 0b1111111 , 0b1101111 , ) NEW_LINE while 1 : NEW_LINE INDENT n = int ( input ( ) ) NEW_LINE if n == - 1 : break NEW_LINE current = 0 NEW_LINE for i in range ( n ) : NEW_LINE INDENT num = NUM [ int ( input ( ) ) ] NEW_LINE print ( format ( current ^ num , ' b ' ) . zfill ( 7 ) ) NEW_LINE current = num NEW_LINE DEDENT DEDENT",
    'MAX = 10000 NEW_LINE arr = [ ] NEW_LINE def SieveOfEratosthenes ( ) : NEW_LINE INDENT prime = [ True ] * MAX NEW_LINE p = 2 NEW_LINE while p * p < MAX : NEW_LINE INDENT if ( prime [ p ] == True ) : NEW_LINE INDENT for i in range ( p * 2 , MAX , p ) : NEW_LINE INDENT prime [ i ] = False NEW_LINE DEDENT DEDENT p += 1 NEW_LINE DEDENT for p in range ( 2 , MAX ) : NEW_LINE INDENT if ( prime [ p ] ) : NEW_LINE INDENT arr . append ( p ) NEW_LINE DEDENT DEDENT DEDENT def isEuclid ( n ) : NEW_LINE INDENT product = 1 NEW_LINE i = 0 NEW_LINE while ( product < n ) : NEW_LINE INDENT product = product * arr [ i ] NEW_LINE if ( product + 1 == n ) : NEW_LINE INDENT return True NEW_LINE DEDENT i += 1 NEW_LINE DEDENT return False NEW_LINE DEDENT if __name__ == " _ _ main _ _ " : NEW_LINE INDENT SieveOfEratosthenes ( ) NEW_LINE n = 31 NEW_LINE if ( isEuclid ( n ) ) : NEW_LINE INDENT print ( " YES " ) NEW_LINE DEDENT else : NEW_LINE INDENT print ( " NO " ) NEW_LINE DEDENT n = 42 NEW_LINE if ( isEuclid ( n ) ) : NEW_LINE INDENT print ( " YES " ) NEW_LINE DEDENT else : NEW_LINE INDENT print ( " NO " ) NEW_LINE DEDENT DEDENT',
    'from mat import sqrt NEW_LINE MAX = 100000 NEW_LINE prime = [ True ] * MAX NEW_LINE arr = [ ] NEW_LINE def SieveOfEratosthenes ( ) : NEW_LINE INDENT for p in range ( 2 , int ( sqrt ( MAX ) ) + 1 ) : NEW_LINE INDENT if prime [ p ] == True : NEW_LINE INDENT for i in range ( p * 2 , MAX , p ) : NEW_LINE INDENT prime [ i ] = False NEW_LINE DEDENT DEDENT DEDENT for p in range ( 2 , MAX ) : NEW_LINE INDENT if prime [ p ] : NEW_LINE INDENT arr . append ( p ) NEW_LINE DEDENT DEDENT DEDENT def isPrimorialPrime ( n ) : NEW_LINE INDENT if not prime [ n ] : NEW_LINE INDENT return False NEW_LINE DEDENT product , i = 1 , 0 NEW_LINE while product < n : NEW_LINE INDENT product *= arr [ i ] NEW_LINE if product + 1 == n or product - 1 == n : NEW_LINE INDENT return True NEW_LINE DEDENT i += 1 NEW_LINE DEDENT return False NEW_LINE DEDENT if __name__ == " _ _ main _ _ " : NEW_LINE INDENT SieveOfEratosthenes ( ) NEW_LINE n = 31 NEW_LINE if ( isPrimorialPrime ( n ) ) : NEW_LINE INDENT print ( " YES " ) NEW_LINE DEDENT else : NEW_LINE INDENT print ( " NO " ) NEW_LINE DEDENT DEDENT'
    ]
    idList = ["aizu_p00855_A",
        "geeksforgeeks_2849_A",
        "aizu_p02296_A",
        "geeksforgeeks_528_A",
        "geeksforgeeks_3249_A",
        "aizu_p00228_A",
        "geeksforgeeks_1326_A",
        "geeksforgeeks_1321_A"]
    javaCodeList = javaCodeList * 16
    pyCodeList = pyCodeList * 16
    idList = idList * 16

    writeDir = "./exptResults_RL/2023-10-25_12-46-14-700604963-10118"
    #rCF = calculateCompilerReward(javaCodeList, "java", writeDir, 'cuda0-1')
    #print (rCF)
    #rCF = calculateCompilerReward(pyCodeList, "python", writeDir, 'cuda0-1')
    #rSF = calculateRuntimeReward(pyCodeList, "python", idList, writeDir, 'cuda0-1')
    #rSF = calculateRuntimeReward(javaCodeList, "java", idList, writeDir, 'cuda0-1')
    #(codeList_pred, lang, probIDs, writeDir, deviceID_str)
    #print (rSF)

    x = np.array([100, 150, 200])
    mu = np.array([125, 150, 890])
    sig = mu/4
    g = gaussian(x, mu, sig)
    print (g)

    #sys.exit(0)

    code = javaCodeList[2]
    splitCode = code.split(" ")
    rList = []
    for i in range(1, len(splitCode) + 1):
        #if (i == len(splitCode)):
        truncCode = " ".join(splitCode[:i])
        print ([truncCode])
        #reward = calculateRuntimeReward([truncCode], "java", [idList[2]], writeDir, "0")
        #reward = calculateCompilerReward([truncCode], "java", writeDir, "0")
        #reward = calculateCompilerRewardModified([truncCode], [code],  "java", writeDir, "0")
        reward = calcCodeBLEUrewardWithMinLenPenalty([truncCode], [code],  "java", writeDir, "0")
        #reward = calcCodeBLEUreward([truncCode], [code], "java", writeDir, "0")
        print (reward)
        rList.append(reward[0])

    print (rList)
