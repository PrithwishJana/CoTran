import os
import sys
import re
import json
import glob
import string

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


def floatReplace_func(match):
    match = match.group()
    return "{:.1f}".format(float(match))

def stringReplace_func(match):
    match = match.group()
    return match.strip("\'")

def checkOutputsSame_runnerFunc(out1, out2):
    if isinstance(out1, str):
        if isinstance(out2, str):
            return checkOutputsSame(out1, out2)
        else:
            for out2_indiv in out2:
                if checkOutputsSame(out1, out2_indiv): return True
    else:
        if isinstance(out2, str):
            for out1_indiv in out1:
                if checkOutputsSame(out1_indiv, out2): return True
        else:
            for out1_indiv in out1:
                for out2_indiv in out2:
                    if checkOutputsSame(out1_indiv, out2_indiv): return True
    return False

def checkOutputsSame(out1, out2):
    #CHECK CASE OF RANDOM
    out1 = out1.replace('\x00', '')
    out2 = out2.replace('\x00', '')
    if (out1 is None) or (out2 is None):
        return False
    if (len(out1.strip())==0) and (len(out2.strip())==0):
        return False
    if "".join(out1.split()).strip() == "".join(out2.split()).strip():  
        return True

    #replaces all floating points or integers --> uniform representation i.e. 1 digit after .
    out1 = re.sub(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', floatReplace_func, out1)
    #removes all punctuations
    out1 = out1.translate(str.maketrans('', '', string.punctuation))

    #replaces all floating points or integers --> uniform representation i.e. 1 digit after .
    out2 = re.sub(r'[-+]?[\d]*[\.][\d]+|[-+]?[\d]+', floatReplace_func, out2)
    #removes all punctuations
    out2 = out2.translate(str.maketrans('', '', string.punctuation))

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

def selectSubdataset(args, programs_py, programs_java, ids, testCases_dict):
    global sourceKeys, ids_alreadyNotMatched

    FINALpyProgList = []
    FINALjavaProgList = []
    FINALidList = []

    assert len(programs_py) == len(programs_java)
    assert len(ids) == len(programs_py)

    num_matches, num_total_checked, num_total = 0, 0, len(programs_py)
    matches_bySource = {}
    randomMatch_bySource = {}
    totalChecked_bySource = {}
    for sk in sourceKeys:
        matches_bySource[sk] = 0
        randomMatch_bySource[sk] = 0
        totalChecked_bySource[sk] = 0

    for progIndx in range(len(programs_py)):
        program_id = ids[progIndx]
        program_py_oneLine = programs_py[progIndx]
        program_java_oneLine = programs_java[progIndx]

        probID, sourceKey = getProbIDKey_fromID(program_id)

        if (probID is None) or (probID not in testCases_dict) or (len(testCases_dict[probID]) == 0):
            print ("\n\n-------------------------------------\n\n", flush=True)
            print ("---> lineNum: " + str(progIndx + 1), flush=True)
            print ("---> id: " + str(ids[progIndx]), "--> ID_NOT_FOUND", flush=True)
            print ("---> probID: " + probID, flush=True)
            continue

        num_total_checked += 1
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

        tcIndx = 0 #FIXED
        tc = testCases_list[tcIndx]
        inputStr = tc[0]
        outputStr = tc[1]
        
        if "projecteuler" in program_id:
            matches_bySource[sourceKey] += 1
            print ("\nMATCHED!! :D", flush=True)
            FINALpyProgList.append(program_py_oneLine)
            FINALjavaProgList.append(program_java_oneLine)
            FINALidList.append(program_id)
            num_matches += 1            
        elif (inputStr is None) and (outputStr is None) and (tc[2].lower() == "random"):
            randomMatch_bySource[sourceKey] += 1
            print ("\nRANDOM-MATCHED!! :D", flush=True)
            FINALpyProgList.append(program_py_oneLine)
            FINALjavaProgList.append(program_java_oneLine)
            FINALidList.append(program_id)
            num_matches += 1
        else:
            console_out_py, program_py = getPyOutput(folderNm, program_py_oneLine, inputStr)
            console_out_java, program_java = getJavaOutput(folderNm + "_2", program_java_oneLine, inputStr)

            print ("---> inputs:\n" + inputStr)
            print ("---> outputs:\n" + str(outputStr))
            print ("---> console_out_py:\n" + console_out_py[:50])
            print ("---> console_out_java:\n" + console_out_java[:50])
            if (checkOutputsSame_runnerFunc(console_out_py, outputStr) and 
                checkOutputsSame_runnerFunc(console_out_java, outputStr)): #pyEqJava
                matches_bySource[sourceKey] += 1
                print ("\npy_EqJv_EqOff MATCHED!! :D", flush=True)
                num_matches += 1
                FINALpyProgList.append(program_py_oneLine)
                FINALjavaProgList.append(program_java_oneLine)
                FINALidList.append(program_id)
            else:
                print ("\nDIDN'T MATCH!! :(", flush=True)

        shutil.rmtree(folderNm, ignore_errors=True)
        shutil.rmtree(folderNm + "_2", ignore_errors=True)

    print ("matches_bySource", matches_bySource)
    print ("randomMatch_bySource", randomMatch_bySource)
    print ("totalChecked_bySource", totalChecked_bySource)

    totalMatches = sum(matches_bySource.values()) + sum(randomMatch_bySource.values())

    print('Success - {}, TotalChecked - {}, Total - {}'.format(
        num_matches, num_total_checked, num_total)
    )

    print ("\nTotal pairs selected:", totalMatches)
    assert len(FINALpyProgList) == len(FINALjavaProgList)
    assert len(FINALjavaProgList) == len(FINALidList)
    assert len(FINALidList) == totalMatches

    return FINALpyProgList, FINALjavaProgList, FINALidList


if __name__ == '__main__':

    testCases_jsonPaths = [
        currPath + "data_LARGE/io_testcases_atcoder.json",
        currPath + "data_LARGE/io_testcases_codeforces.json",
        currPath + "data_LARGE/io_testcases_leetcode.json",
        currPath + "data_LARGE/io_testcases_codejam.json",
        currPath + "data_LARGE/io_testcases_geeksforgeeks.json",
        currPath + "data_LARGE/io_testcases_projecteuler.json",
        currPath + "data_LARGE/io_testcases_aizu.json"
    ]
                

    testCases_dict = {}
    for jsonPath in testCases_jsonPaths:
        with open(jsonPath, 'r') as j:
            if jsonPath.endswith(".json"):
                jsonDict = json.loads(j.read())
        
        tmpDict = dict((key, value[:1]) for (key, value) in jsonDict.items())
        testCases_dict = dict(list(testCases_dict.items()) + list(tmpDict.items()))

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_type", type=str, help='train/test/valid')
    parser.add_argument("--input_folder", type=str)
    parser.add_argument("--debug", type=bool, default="1", help='Whether to print debugging outputs')
    parser.add_argument("--writeDir", type=str, default = "./junk", help='Directory where .java, .class, .py files will be written')
    args = parser.parse_args()

    pyFilePath = os.path.join(args.input_folder, args.input_type + ".java-python.python")
    programs_py = []
    with open(pyFilePath, encoding='utf8') as f:
        for line in f:
            programs_py.append(line.strip())

    javaFilePath = os.path.join(args.input_folder, args.input_type + ".java-python.java")
    programs_java = []
    with open(javaFilePath, encoding='utf8') as f:
        for line in f:
            programs_java.append(line.strip())

    idFilePath = os.path.join(args.input_folder, args.input_type + ".java-python.id")
    ids = []
    with open(idFilePath, encoding='utf8') as f:
        for line in f:
            ids.append(line.strip())

    pyProgList, javaProgList, idList = selectSubdataset(args, programs_py, programs_java, ids, testCases_dict)

    assert len(pyProgList) == len(javaProgList)
    assert len(javaProgList) == len(idList)

    with open("../FIN" + args.input_type + ".java-python.python", 'w') as f:
        for pyLine in pyProgList:
            f.write(f"{pyLine}\n")

    with open("../FIN" + args.input_type + ".java-python.java", 'w') as f:
        for jvLine in javaProgList:
            f.write(f"{jvLine}\n")

    with open("../FIN" + args.input_type + ".java-python.id", 'w') as f:
        for idLine in idList:
            f.write(f"{idLine}\n")
    