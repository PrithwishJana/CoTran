from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
import shutil, time, random, subprocess, os, re, copy
import torch
from pygments.lexers.jvm import JavaLexer
from pygments.token import Token

def calculateCompilerReward(codeList, lang, writeDir, deviceID_str):
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

    if lang == 'java':
        # set up tokenizers
        javalexer = JavaLexer()

        errMetric_list_perChunk = []
        paths_allProgs = [] #list of lists
        folders_allProgs = [] #list of lists
        tokensLen_allProgs = [] #list of lists 

        for progIndx, oneLineProg in enumerate(codeList):
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

        # use javac and subprocess call, to get stderr for each code -----------------
        errorlog_content_allProgs = subprocess.Popen(["javac"] + ["-cp", ".:{}".format(extJavaLibraries)] + 
                                                        ["-Xmaxerrs", str(len(paths_allProgs) * 750)] +
                                                        paths_allProgs, 
                                                        stderr = subprocess.PIPE, text = True).stderr.read()

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
                rewardAllProgs[progIndx] = (min_error_position * 1.0 / (numLinesInJavaProg + 1))
                if DEBUG_FLAG: print (str(min_error_position * 1.0) + " / " + str(numLinesInJavaProg + 1)
                                        + " = " + str(rewardAllProgs[progIndx]))
            else:
                rewardAllProgs[progIndx] = 1.0
            if DEBUG_FLAG: print ("rewardAllProgs[{}]".format(progIndx), rewardAllProgs[progIndx])

    else:
        raise NotImplementedError

    shutil.rmtree(folderNm, ignore_errors = True)
    rewardAllProgs = [(((x - 0) / (0.8 - 0)) - 1.0) if x < 0.8 else (((x - 0.8) / (1.0 - 0.8)) + 0.0) for x in rewardAllProgs]
    rewardAllProgs = [torch.tensor(float(x)) for x in rewardAllProgs]
    return rewardAllProgs


#================== MAIN ======================
if __name__ == '__main__':
    javaCodeList = ['import java . io . BufferedReader ; import java . io . IOException ; import java . io . InputStreamReader ; public class Main { public static void main ( String [ ] args ) throws IOException { BufferedReader br = new BufferedReader ( new InputStreamReader ( System . in ) ) ; String str = br . readLine ( ) ; String [ ] s ; int i , j , n ; s = str . split ( " " , 0 ) ; j = 0 ; n = Integer . parseInt ( s [ 0 ] ) ; System . out . println ( j ) ; } }',
    'import java . io . * ; import java . util . * ; public class Main { List < List < Integer > > opList ; static List < Integer > opList ; public static void main ( String [ ] args ) { new Main ( ) ; } public void run ( ) { try { read ( ) ; solve ( ) ; } catch ( IOException e ) { e . printStackTrace ( ) ; } } private void read ( ) throws IOException { if ( System . getProperty ( " ONLINE _ JUDGE " )!=null ) { File inputFile = new File ( " input . txt " ) ; File outputFile = new File ( " output . txt " ) ; File inputFile = new File ( " input . txt " ) ; output = new ArrayList < List < Integer > > ( ) ; opList . add ( input ) ; opList . add ( output ) ; } long round = MOD / 1000000007 ; long result = round * 1000 % 1000 ; if ( result > 1 ) { l = result / 2 ; result = result / 2 ; } else { l = result / 2 ; result = result / 2 ; } result = round * 1000 % 1000 ; out . println ( result ) ; } private static void solve ( ) throws IOException { opList . clear ( ) ; opList . add ( null ) ; deal ( ) ; done ( ) ; } private static void deal ( ) throws IOException { if ( System . getProperty ( " ONLINE _ JUDGE " ) == null ) { try { open ( " MATH " ) ; } catch ( IOException e ) { e . printStackTrace ( ) ; } long start = System . currentTimeMillis ( ) ; for ( int i = 0 ; i < opList . size ( ) ; i ++ ) { try { System . setIn ( new FileInputStream ( opList . get ( i ) ) ) ; } catch ( Exception e ) { e . printStackTrace ( ) ; } catch ( Exception e ) { e . printStackTrace ( ) ; } } final int mod = ( int ) ( System . currentTimeMillis ( ) / 1000 ) ; final int poll = ( int ) ( ( System . currentTimeMillis ( ) / 2 ) * 1000 + UIVE_TIME ) % 60 + UFACTTER ) ; for ( int i = 0 ; i < 5 ; i ++ ) { if ( opList . get ( i ) . size ( ) > 1 ) { e . printStackTrace ( ) ; System . exit ( 1 ) ; } } long end =', 
    'import java . util . Scanner ; import java . util . stream . IntStream ; public class Main { static IntStream REPS ( int v ) { return IntStream . rangeClosed ( 0 , v ) ; } static IntStream REPS ( int l , int r ) { return IntStream . rangeClosed ( l , r ) ; } static IntStream INS ( int n ) { return REPS ( n ) . map ( i -> getInt ( ) ) ; } static Scanner s = new Scanner ( System . in ) ; static int getInt ( ) { return Integer . parseInt ( s . next ( ) ) ; } public static void main ( String [ ] $ ) { int a = getInt ( ) , b = getInt ( ) ; System . out . println ( a == 0 ? b : Math . min ( Math . min ( a + b , b ) , a ) ) ; } }', 
    "import java . io . BufferedReader ; import java . io . IOException ; import java . io . InputStreamReader ; import java . util . StringTokenizer ; public class PrintTheNumber { public static void main ( String [ ] args ) throws IOException { BufferedReader br = new BufferedReader ( new InputStreamReader ( System . in ) ) ; StringTokenizer st ; char c ; PrintStream out = new PrintStream ( System . out ) ; c = new StringTokenizer ( br . readLine ( ) ) ; out . println ( ( int ) st . nextToken ( ) - '0' ) ; out . flush ( ) ; } String next ( ) throws IOException { while ( st == null || ! st . hasMoreTokens ( ) ) st = new StringTokenizer ( br . readLine ( ) ) ; return st . nextToken ( ) ; } int nextInt ( ) throws IOException { return Integer . parseInt ( next ( ) ) ; } long nextLong ( ) throws IOException { return Long . parseLong ( next ( ) ) ; } double nextDouble ( ) throws IOException { return Double . parseDouble ( next ( ) ) ; } }", 
    'import java . util . * ; import java . io . * ; public class Main { public static void main ( String args [ ] ) throws IOException { FastReader in = new FastReader ( ) ; PrintWriter out = new PrintWriter ( System . out ) ; int t = 1 ; while ( t -- > 0 ) { int n = in . nextInt ( ) ; if ( n == 1 ) out . println ( 1 ) ; else { out . println ( 2 ) ; } } out . close ( ) ; } long gcd ( long a , long b ) { return ( b == 0 ) ? a : gcd ( b , a % b ) ; } static class FastReader { BufferedReader br ; StringTokenizer st ; public FastReader ( ) { br = new BufferedReader ( new InputStreamReader ( System . in ) ) ; } String next ( ) { while ( st == null || ! st . hasMoreElements ( ) ) { try { st = new StringTokenizer ( br . readLine ( ) ) ; } catch ( IOException e ) { e . printStackTrace ( ) ; } } return st . nextToken ( ) ; } int nextInt ( ) { return Integer . parseInt ( next ( ) ) ; } long nextLong ( ) { return Long . parseLong ( next ( ) ) ; } double nextDouble ( ) { return Double . parseDouble ( next ( ) ) ; } String nextLine ( ) { String str = " " ; try { str = br . readLine ( ) ; } catch ( IOException e ) { e . printStackTrace ( ) ; } return str ; } } }', 
    'import java . util . * ; public class Main { public static void main ( String [ ] agrs ) { Scanner sc = new Scanner ( System . in ) ; int [ ] a = { 1 , 4 , 8 , 16 , 128 , 256 , 512 , 512 } ; Arrays . sort ( a ) ; System . out . println ( String . valueOf ( a ) ) ; } }', 
    'import java . util . * ; public class Main { public static class Terminal { char c ; int p ; public Terminal ( char c , int p ) { this . c = c ; this . p = p ; } } } class Pair implements Comparable { int from ; int p ; int q ; public Pair ( int from , int p ) { this . from = from ; this . p = p ; } public int compareTo ( Pair p ) { if ( this . p < p . p ) return - 1 ; else { return 1 ; } } } public static void main ( String [ ] args ) { Scanner sc = new Scanner ( System . in ) ; int n = sc . nextInt ( ) ; int d = sc . nextInt ( ) ; System . out . println ( n + d ) ; } }', 
    'public class Main { public void run ( java . io . InputStream in , java . io . PrintStream out ) { java . util . Scanner sc = new java . util . Scanner ( in ) ; int i , n ; int [ ] a ; a = new int [ 10000 ] ; n = 0 ; for ( ; sc . hasNext ( ) ; ) { n = 1 - n ; for ( i = 0 ; i < n ; ) if ( a [ i ] == 1 ) a [ i ] = 0 ; i ++ ; } sc . close ( ) ; } public static void main ( String [ ] args ) { ( new Main ( ) ) . run ( System . in , System . out ) ; } }'
    ]
    javaCodeList = javaCodeList * 16

    writeDir = "./exptResults_RL/2023-10-25_12-46-14-700604963-10118"
    r = calculateCompilerReward(javaCodeList, "java", writeDir, 'cuda0-1')
    print (r)