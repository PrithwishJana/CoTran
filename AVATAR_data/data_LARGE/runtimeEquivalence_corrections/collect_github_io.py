import shutil, time, random, os, glob, sys, re, json
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE

spclCases = {   "geeksforgeeks_5145_A": [["10\n20\n", None]],
                "geeksforgeeks_5144_A": [["10\n20\n", None]],
                "geeksforgeeks_4247_A": [["abxhydl\nabxhydl\n", None]]} #line 285 of test check
#include \0 in encoding logic 

def getPythonOutput(oneLineCode, inputs = None):
    global writeDir, pyprocessor

    public_class_name = 'main'
    if "public class" in oneLineCode:
        public_class_name = oneLineCode.split("public class", 1)[1].split()[0]

    subfolderExists = True
    while subfolderExists:
        time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
        folderNm = os.path.join(writeDir, time_rand_str)
        
        subfolderExists = os.path.exists(folderNm)
        if not subfolderExists:
            os.makedirs(folderNm, exist_ok = False)

    program = pyprocessor.detokenize_code(oneLineCode)
    filename = os.path.join(folderNm, '{}.py'.format(public_class_name))
    with open(filename, 'w', encoding='utf8') as fw:
        fw.write(program)

    command = ["python", filename]
    if inputs is None:
        p = run(command, stdout=PIPE)
    else:
        p = run(command, input = inputs.encode('utf-8'), stdout=PIPE)
    console_out = p.stdout.decode("utf-8")
    shutil.rmtree(folderNm, ignore_errors=True)
    return console_out, program

def getJavaOutput(oneLineCode, inputs = None):
    global writeDir, jprocessor

    public_class_name = 'main'
    if "public class" in oneLineCode:
        tokens = oneLineCode.split("public class", 1)
        if len(tokens) == 2 and len(tokens[1]) > 0:
            public_class_name = tokens[1].split()[0]
    elif "public final class" in oneLineCode:
        tokens = oneLineCode.split("public final class", 1)
        if len(tokens) == 2 and len(tokens[1]) > 0:
            public_class_name = tokens[1].split()[0]

    subfolderExists = True
    while subfolderExists:
        time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
        folderNm = os.path.join(writeDir, time_rand_str)
        
        subfolderExists = os.path.exists(folderNm)
        #print ("exist check:", subfolderExists)
        if not subfolderExists:
            os.makedirs(folderNm, exist_ok = False)
            #print ("folder created:", folderNm)

    program = jprocessor.detokenize_code(oneLineCode)
    #print ("\n\n", program, "\n\n")
    filename = os.path.join(folderNm, '{}.java'.format(public_class_name))
    with open(filename, 'w', encoding='utf8') as fw:
        fw.write(program)

    command1 = ["javac", "-cp", "{}:{}".format(folderNm, extJavaLibraries), filename] 
    try:
        run(command1)
        classFiles = glob.glob(os.path.join(folderNm, "*.class"))
        if len(classFiles) == 1:
            classFile = classFiles[0]
        else:
            classFile = None
            for cf in classFiles:
                if public_class_name + ".class" in cf:
                    classFile = cf
        assert classFile is not None
        print ("classFiles", classFiles)
        head, tail = os.path.split(classFile)
        command2 = ["java", "-cp", "{}:{}".format(folderNm, extJavaLibraries), 
                    tail.split('.class')[0]]
        if inputs is None:
            p = run(command2, stdout=PIPE)
        else:
            p = run(command2, input = inputs.encode('utf-8'), stdout=PIPE)
        console_out = p.stdout.decode("utf-8")
    except Exception as e:
        print ("e", e)
        return None, oneLineCode

    shutil.rmtree(folderNm, ignore_errors=True)

    return console_out, program

def floatReplace_func(match):
    match = match.group()
    return "{:.1f}".format(float(match))

def stringReplace_func(match):
    match = match.group()
    return match.strip("\'")

def checkOutputsSame(out1, out2):
    #CHECK CASE OF RANDOM
    #remove comma and [], to match [1,2,3,4] with 1 2 3 4
    #print ("checking...")
    if (out1 is None) or (out2 is None):
        return False
    #UNCOMMENT AT REAL TEST TIME...
    #can distinguish between 1 2 1 and 121
    #if "".join(out1.split()).strip() == "".join(out2.split()).strip():  
    #    return True
    #out1_matches = list(set(re.findall(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', out1)))
    #print ("out1_matches", out1_matches)
    #for mat1 in out1_matches:
    #print ("out1", out1)
    out1 = re.sub(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', floatReplace_func, out1)
    out1 = re.sub(r'\'.*?\'', stringReplace_func, out1)
    #    #out1 = out1.replace(mat1, "{:.1f}".format(float(mat1)))
    #    print ("xxx", "(" + str(mat1) + ")", "({:.1f})".format(float(mat1)))
    #print ("out1", out1)
    #out2_matches = list(set(re.findall(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', out2)))
    #print ("out2_matches", out2_matches)
    #print ("out2", out2)
    out2 = re.sub(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', floatReplace_func, out2)
    out2 = re.sub(r'\'.*?\'', stringReplace_func, out2)
    #print ("out2", out2)
    #for mat2 in out2_matches:
    #    out2 = re.sub(r'[^-+\.\d]' + re.escape(mat2) + r'[^-+\.\d]', "{:.1f}".format(float(mat2)), out2)
    #    #out2.replace(mat2, "{:.1f}".format(float(mat2)))
    #    print ("out2", out2)
    out1List = out1.strip().split()
    out2List = out2.strip().split()
    #print ("chck1", out1List, out2List)
    #print ("chck2", "".join(out1List), "".join(out2List))

    #print ("out1List", out1List)
    #print ("out2List", out2List)
    #print ("chck2", out1List, out2List)
    return "".join(out1List).lower() == "".join(out2List).lower()
    #"".join(pyOut.split()).strip() == "".join(javaOut.split()).strip()



if __name__ == '__main__':
    testCasesDict = {}

    writeDir = "./junk"

    root_folder = "../../third_party"
    extJavaLibraries = "../../data_extLibraries/"
    jprocessor = JavaProcessor(root_folder=root_folder)
    pyprocessor = PythonProcessor(root_folder=root_folder)
    idFilePaths = ["../{}.java-python.id".format(x) for \
                        x in ["valid", "test", "train"]]
    oneLine_codePaths_java = ["./{}.java-python.java".format(x) for \
                        x in ["valid", "test", "train"]]
    oneLine_codePaths_py = ["./{}.java-python.python".format(x) for \
                        x in ["valid", "test", "train"]]

    #{"id": ..., "inputs": [], "outputs": []}

    oneLine_javaCode_listofList = []
    oneLine_pyCode_listofList = []
    for fileIndx in range(len(oneLine_codePaths_java)):
        with open(oneLine_codePaths_java[fileIndx]) as file:
            oneLine_javaCode_listofList.append([line.strip() for line in file])
        with open(oneLine_codePaths_py[fileIndx]) as file:
            oneLine_pyCode_listofList.append([line.strip() for line in file])

    xx = 0
    for fileIndx in range(0, len(idFilePaths)):
        with open(idFilePaths[fileIndx]) as file:
            idList = [line.strip() if "geeksforgeeks" in line else "" for line in file]
        for idIndx in range(0, len(idList)): #RESET TO 0 !!!!!!!!!!!!!!!!!!!! #31909 train
            extraComment = None
            if len(idList[idIndx]) != 0:
                javaCode = oneLine_javaCode_listofList[fileIndx][idIndx]
                pyCode = oneLine_pyCode_listofList[fileIndx][idIndx]

                SPCL = False

                if idList[idIndx] in spclCases:
                    SPCL = True
                    print ("inputs", spclCases[idList[idIndx]][0][0])
                    javaOut, javaDecodedCode = getJavaOutput(javaCode, spclCases[idList[idIndx]][0][0])
                    pyOut, pyDecodedCode = getPythonOutput(pyCode, spclCases[idList[idIndx]][0][0])
                else:
                    #print ("javaCode", javaCode)
                    javaOut, javaDecodedCode = getJavaOutput(javaCode)
                    #print (javaDecodedCode, flush=True)
                    #print ("\n\n", javaOut, flush=True)

                    #print ("pyCode", pyCode)
                    pyOut, pyDecodedCode = getPythonOutput(pyCode)
                    #print (pyDecodedCode, flush=True)
                    #print ("\n\n", pyOut, flush=True)

                print ("\n---------------------------------------\n", flush=True)

                xx = checkOutputsSame(pyOut, javaOut)
                try:
                    print ("\n\n", idFilePaths[fileIndx], "line: {}".format(idIndx+1))
                    if not xx:
                        assert False
                    out = pyOut
                    #print ("pyOut ({}) matches javaOut ({})".format(pyOut, javaOut))
                except:
                    if "random" in javaDecodedCode.lower() and "random" in pyDecodedCode:
                        print ("pyOut ({}) didn't match javaOut ({}), but random present".format(pyOut, javaOut))
                        out = ""
                        extraComment = "random"
                    else:
                        print ("pyOut ({}) didn't match javaOut ({})".format(pyOut, javaOut))
                        print (javaDecodedCode, pyDecodedCode)
                        sys.exit(0)

                if not SPCL:
                    list2Write = ["", out]
                else:
                    list2Write = [spclCases[idList[idIndx]][0][0], out]
                if extraComment is not None:
                    list2Write = [None, None, extraComment]
                if idList[idIndx] in testCasesDict:
                    testCasesDict[idList[idIndx]].append(list2Write)
                else:
                    testCasesDict[idList[idIndx]] = [list2Write]
                #print (testCasesDict)

                #if "input ( )" in pyCode:
                #    xx += 1

        #break
        #idList = list(set(idList) - set([""]))
        #xx += (len(idList))
        #print (xx)

    shutil.rmtree(writeDir, ignore_errors=True)
    with open('io_testcases_geeksforgeeks.json', 'w') as fp:
        json.dump(testCasesDict, fp, indent=4)
