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
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE, Popen
import shutil, time, random

currPath = "../../../AVATAR_data/" #"./AVATAR_data/"

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

sourceKeys = ["aizu", "atcoder", "codeforces", "codejam", "geeksforgeeks",
                "leetcode", "projecteuler"]

def getProbIDKey_fromID(id):
    global sourceKeys
    for sourceKey in sourceKeys:
        if sourceKey in id:
            if sourceKey in ["codeforces", "atcoder", "codejam", "aizu"]:
                if id.count("_") == 2:
                    return id, sourceKey
                else:
                    return '_'.join(id.split('_')[:-2]), sourceKey
            elif (sourceKey in ["leetcode", "geeksforgeeks", "projecteuler"]):
                return id, sourceKey
    return None, None

def addOutputToDict(myDict, id, inp, out):
    if id in myDict: 
        if isinstance(myDict[id][0][1], str):
            if checkOutputsSame(myDict[id][0][1], out):
                return myDict
            myDict[id][0][1] = [myDict[id][0][1]]
        else:
            for earlierOuts in myDict[id][0][1]:
                if checkOutputsSame(earlierOuts, out):
                    return myDict
        myDict[id][0][1].append(out)
    else:
        myDict[id] = [[inp, out]]
    return myDict


def floatReplace_func(match):
    match = match.group()
    return "{:.1f}".format(float(match))

def stringReplace_func(match):
    match = match.group()
    return match.strip("\'")

def checkOutputsSame(out1, out2):
    #CHECK CASE OF RANDOM
    out1 = out1.replace('\x00', '')
    out2 = out2.replace('\x00', '')
    if (out1 is None) or (out2 is None):
        return False
    if "".join(out1.split()).strip() == "".join(out2.split()).strip():  
        return True

    #replaces all floating points or integers --> uniform representation i.e. 1 digit after .
    out1 = re.sub(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', floatReplace_func, out1)
    #removes all punctuations
    #out1 = out1.translate(str.maketrans('', '', string.punctuation))
    #replaces all strings surrounded by quotations --> without quotes
    out1 = re.sub(r'\'.*?\'', stringReplace_func, out1)

    #replaces all floating points or integers --> uniform representation i.e. 1 digit after .
    out2 = re.sub(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', floatReplace_func, out2)
    #removes all punctuations
    #out2 = out2.translate(str.maketrans('', '', string.punctuation))
    #replaces all strings surrounded by quotations --> without quotes
    out2 = re.sub(r'\'.*?\'', stringReplace_func, out2)

    #removes all whitespaces
    out1List = out1.strip().split()
    out2List = out2.strip().split()
    #changes to lowercase
    return "".join(out1List).lower() == "".join(out2List).lower()

def getPyOutput(folderNm, oneLineProg, inputStr):
    program = pyprocessor.detokenize_code(oneLineProg)
    program = program.replace('input.txt', os.path.join(folderNm, 'input.txt'))
    program = program.replace('output.txt', os.path.join(folderNm, 'output.txt'))

    filename = os.path.join(folderNm, 'main.py')
    with open(filename, 'w', encoding='utf8') as fw:
        fw.write(program)

    with open(os.path.join(folderNm, 'input.txt'), 'w', encoding='utf8') as fw:
        fw.write(inputStr)

    command = ["python", filename]
    #p = run(command, input = inputStr.encode('utf-8'), stdout = PIPE, env = myenv)
    #console_out = p.stdout.decode("utf-8")

    try:
        p = run(command, input = inputStr.encode('utf-8'), stdout=PIPE, env = myenv, timeout=40)
        console_out = p.stdout.decode("utf-8")
        if os.path.exists(os.path.join(folderNm, 'output.txt')):
            with open(os.path.join(folderNm, 'output.txt'), 'r') as f:
                console_out = f.read()
    except:
        return "TIMEOUT ENCOUNTERED-PY", program
    
    return console_out, program

def getJavaOutput(folderNm, oneLineProg, inputStr):
    global extJavaLibraries
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
    program = program.replace('input.txt', os.path.join(folderNm, 'input.txt'))
    program = program.replace('output.txt', os.path.join(folderNm, 'output.txt'))

    filename = os.path.join(folderNm, '{}.java'.format(public_class_name))
    with open(filename, 'w', encoding='utf8') as fw:
        fw.write(program)

    with open(os.path.join(folderNm, 'input.txt'), 'w', encoding='utf8') as fw:
        fw.write(inputStr)

    command1 = ["javac", "-cp", "{}:{}".format(folderNm, extJavaLibraries), filename] 
    run(command1)

    classFiles = glob.glob(os.path.join(folderNm, "*.class"))
    if len(classFiles) == 1:
        classFile = classFiles[0]
    else:
        classFile = None
        for cf in classFiles:
            if public_class_name + ".class" in cf:
                classFile = cf
    if classFile is None:
        return "MULTIPLE CLASSES, BUT NONE PUBLIC", program

    head, tail = os.path.split(classFile)
    command2 = ["java", "-cp", "{}:{}".format(folderNm, extJavaLibraries), 
                tail.split('.class')[0]]
    #p = Popen(command2, input = inputStr.encode('utf-8'), stdout=PIPE, stderr=PIPE)
    #output, error = p.communicate()
    #if p.returncode != 0: 
    #    print (p.returncode, output, error)
    #    return "EXCEPTION ENCOUNTERED", program
    #console_out = output.decode("utf-8")

    try:
        p = run(command2, input = inputStr.encode('utf-8'), stdout=PIPE, stderr=PIPE, timeout=20)
        if os.path.exists(os.path.join(folderNm, 'output.txt')):
            with open(os.path.join(folderNm, 'output.txt'), 'r') as f:
                console_out = f.read()
            return console_out, program
        if p.returncode != 0:
            print (p.returncode, p.stderr.decode("utf-8"))
            return "EXCEPTION ENCOUNTERED-JV", program
        console_out = p.stdout.decode("utf-8")
    except:
        return "TIMEOUT ENCOUNTERED-JV", program
    
    return console_out, program

def check_runtimeOut(args, programs_py, programs_java, ids, testCases_dict):
    global sourceKeys, ids_alreadyNotMatched

    NEW_testCases_dict = {}

    assert len(programs_py) == len(programs_java)

    num_total = len(programs_py)
    pyEqJv_neqOff_empty_bySource = {}
    pyEqJv_neqOff_NOTempty_bySource = {}
    pyEqJv_EqOff_bySource = {}
    randomMatch_bySource = {}
    pyNeqJv_bySource = {}
    totalChecked_bySource = {}

    for sk in sourceKeys:
        pyEqJv_neqOff_empty_bySource[sk] = 0
        pyEqJv_neqOff_NOTempty_bySource[sk] = 0
        pyEqJv_EqOff_bySource[sk] = 0
        randomMatch_bySource[sk] = 0
        pyNeqJv_bySource[sk] = 0
        totalChecked_bySource[sk] = 0

    assert len(ids) == len(programs_py)

    for progIndx in range(len(programs_py)):
        probID, sourceKey = getProbIDKey_fromID(ids[progIndx])

        #if probID in ids_alreadyNotMatched:
        #    continue
        #ids_alreadyNotMatched.append(probID)
        #ids_alreadyNotMatched = list(set(ids_alreadyNotMatched))

        program_py = programs_py[progIndx]
        program_java = programs_java[progIndx]

        if (probID is None) or (probID not in testCases_dict) or (len(testCases_dict[probID]) == 0):
            if "codejam" in ids[progIndx]:
                print ("\n\n-------------------------------------\n\n", flush=True)
                print ("---> lineNum: " + str(progIndx + 1), flush=True)
                print ("---> id: " + str(ids[progIndx]), flush=True)
                print ("---> probID: " + probID, flush=True)
            continue

        totalChecked_bySource[sourceKey] += 1

        subfolderExists = True
        while subfolderExists:
            time_rand_str = str(int(round(time.time() * 1000))) + "_" + str(random.randint(1000,9999))
            folderNm = os.path.join(args.writeDir, time_rand_str)
            subfolderExists = os.path.exists(folderNm)
            if not subfolderExists:
                os.makedirs(folderNm, exist_ok = False)
                os.makedirs(folderNm + "_2", exist_ok = False)

        testCases_list = testCases_dict[probID]
        print ("\n\n-------------------------------------\n\n", flush=True)
        print ("---> lineNum: " + str(progIndx + 1), flush=True)
        print ("---> probID: " + probID, flush=True)
        for tcIndx in range(1):
            tc = testCases_list[tcIndx]
            inputStr = tc[0]
            outputStr = tc[1]
            NEW_testCases_dict = addOutputToDict(NEW_testCases_dict, probID, inputStr, outputStr)
            #NEW_testCases_dict[probID] = [[inputStr, outputStr]]
            if (inputStr is None) and (outputStr is None) and (tc[2] == "random"):
                randomMatch_bySource[sourceKey] += 1
                print ("\n---> console_out:\n" + console_out, "\nRANDOM-MATCHED!! :D", flush=True)

            console_out_py, program_py = getPyOutput(folderNm, program_py, inputStr)
            console_out_java, program_java = getJavaOutput(folderNm + "_2", program_java, inputStr)

            if checkOutputsSame(console_out_py, console_out_java): #pyEqJava
                if ((not checkOutputsSame(console_out_py, outputStr)) or (
                                not checkOutputsSame(console_out_java, outputStr))): #neqOff

                    if (len(console_out_py.strip()) != 0) and \
                        (len(console_out_java.strip()) != 0) and \
                        ("ENCOUNTERED-PY" not in console_out_py) and \
                        ("ENCOUNTERED-JV" not in console_out_java):

                        NEW_testCases_dict = addOutputToDict(NEW_testCases_dict, probID, inputStr, console_out_py)
                        pyEqJv_neqOff_NOTempty_bySource[sourceKey] += 1
                    else:
                        pyEqJv_neqOff_empty_bySource[sourceKey] += 1
                    
                    if args.debug and len(console_out_py.strip()) == 0:
                        print ("---> inputs:\n" + inputStr)
                        print ("---> outputs:\n" + outputStr)
                        print ("\n---> py-code:\n" + program_py)
                        print ("\n---> java-code:\n" + program_java)
                    print ("---> console_out_py:\n" + console_out_py[:50])
                    print ("---> console_out_java:\n" + console_out_java[:50])
                    
                    print ("\npyEqJv_neqOff_MATCHED!! :D\n", flush=True)
                else:
                    pyEqJv_EqOff_bySource[sourceKey] += 1
                    '''
                    if args.debug:
                        print ("---> inputs:\n" + inputStr)
                        print ("---> outputs:\n" + outputStr)
                    '''
                    print ("\n---> outputStr:\n" + outputStr, "\npyEqJv_eqOff_MATCHED!! :D", flush=True)
                
            else:
                pyNeqJv_bySource[sourceKey] += 1
                if args.debug:
                    print ("---> inputs:\n" + inputStr)
                    print ("---> outputs:\n" + outputStr)
                    print ("\n---> py-code:\n" + program_py)
                    print ("\n---> java-code:\n" + program_java)
                    print ("---> console_out_py:\n" + console_out_py[:50])
                    print ("---> console_out_java:\n" + console_out_java[:50])
            
                print ("\npyNeqJv_DIDN'T MATCH!! :(", flush=True)
                #sys.exit(0) #uncomment if you want the code to terminate on first non-match

        shutil.rmtree(folderNm, ignore_errors=True)
        shutil.rmtree(folderNm + "_2", ignore_errors=True)

    print ("pyEqJv_neqOff_NOTempty_bySource", pyEqJv_neqOff_NOTempty_bySource)
    print ("pyEqJv_neqOff_empty_bySource", pyEqJv_neqOff_empty_bySource)
    print ("pyEqJv_EqOff_bySource", pyEqJv_EqOff_bySource)
    print ("randomMatch_bySource", randomMatch_bySource)
    print ("pyNeqJv_bySource", pyNeqJv_bySource)
    print ("totalChecked_bySource", totalChecked_bySource)
    return NEW_testCases_dict


if __name__ == '__main__':
    '''
    jsonOrigPath = currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_aizuORIG.json"
    with open(jsonOrigPath, 'r') as j:
        jsonDict = json.loads(j.read())   
    newDict = dict((key, value[0:1])
                                for (key, value) in jsonDict.items()
                                if len(value) > 0) 
    with open(jsonOrigPath.replace("ORIG", "TMP"), 'w') as fp:
        json.dump(newDict, fp, indent=4)
    '''
    
    #ids_alreadyNotMatched = []
    testCases_jsonPaths = [currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_codejamTMP.json"]
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_atcoder.json",
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_codeforces.json",
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_leetcode.json",
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_codejam.json",
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_geeksforgeeks.json",
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_projecteuler.json"
    #currPath + "data_LARGE/runtimeEquivalence_corrections/io_testcases_aizu.json"

    assert len(testCases_jsonPaths) == 1
                

    testCases_dict = {}
    for jsonPath in testCases_jsonPaths:
        with open(jsonPath, 'r') as j:
            if jsonPath.endswith(".json"):
                jsonDict = json.loads(j.read())
        
        #----CORRECTIONS----
        if "atcoder" in jsonPath:
            tmpDict = dict((key.upper().replace('ATCODER_', 'atcoder_'), value[:1]) \
                                for (key, value) in jsonDict.items())
        else:
            tmpDict = dict((key, value[:1]) for (key, value) in jsonDict.items())
        jsonDict = tmpDict
        #---- ----
        testCases_dict = dict(list(testCases_dict.items()) + list(jsonDict.items()))

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_type", type=str, help='train/test/valid')
    parser.add_argument("--id_file", type=str, help='Source ID file')
    parser.add_argument("--debug", type=bool, default="1", help='Whether to print debugging outputs')
    parser.add_argument("--writeDir", type=str, default = "./junk", help='Directory where .java, .class, .py files will be written')
    args = parser.parse_args()

    pyFilePath = args.input_type + ".java-python.python"
    programs_py = []
    with open(pyFilePath, encoding='utf8') as f:
        for line in f:
            programs_py.append(line.strip())

    javaFilePath = args.input_type + ".java-python.java"
    programs_java = []
    with open(javaFilePath, encoding='utf8') as f:
        for line in f:
            programs_java.append(line.strip())

    ids = []
    with open(args.id_file, encoding='utf8') as f:
        for line in f:
            ids.append(line.strip())

    NEW_testCases_dict = check_runtimeOut(args, programs_py, programs_java, ids, testCases_dict)

    print (NEW_testCases_dict)
    with open(testCases_jsonPaths[0].replace("TMP", "-{}".format(args.input_type)), 'w') as fp:
        json.dump(NEW_testCases_dict, fp, indent=4)
    