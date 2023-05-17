from os import listdir
import os, re, shutil

projEulerRoot = '/home/pjana/scratch/AVATAR_data/'
projEuler_folderNm = 'ProjectEuler'

javaLibDependencies = {"reverse": [],
                        "isPalindrome": ["reverse"],
                        "sqrt": [],
                        "isSquare": ["sqrt"],
                        "pow": [],
                        "powMod": [],
                        "reciprocalMod": [],
                        "factorial": [],
                        "binomial": ["factorial"],
                        "gcd": [],
                        "isPrime": ["sqrt"],
                        "listPrimality": ["sqrt"],
                        "listPrimes": ["listPrimality", "sqrt"],
                        "listSmallestPrimeFactors": ["sqrt"],
                        "totient": ["sqrt"],
                        "listTotients": [],
                        "nextPermutation": []}

pythonLibDependencies = {"popcount": [],
                        "sqrt": [],
                        "is_square": ["sqrt"],
                        "is_prime": ["sqrt"],
                        "list_primality": ["sqrt"],
                        "list_primes": ["list_primality", "sqrt"],
                        "prime_generator": ["sqrt"],
                        "list_smallest_prime_factors": ["sqrt"],
                        "list_totients": [],
                        "binomial": [],
                        "next_permutation": []}

projEulerPath = os.path.join(projEulerRoot, projEuler_folderNm)
if os.path.exists(projEulerPath):
    shutil.rmtree(projEulerPath)
shutil.copytree(os.path.join(projEulerRoot, projEuler_folderNm + "_ORIGNew"), projEulerPath)

f = open(projEulerPath + "/" + "Library.java", 'r', encoding='utf8')
Library_fileStr = f.read()
f.close()

f = open(projEulerPath + "/" + "eulerlib.py", 'r', encoding='utf8')
eulerlib_fileStr = f.read()
f.close()

for contest_dir in listdir(projEulerPath):
    # contest_dir = p001, p002, ...
    if contest_dir == '.DS_Store':
        continue
    if contest_dir[0] != 'p': 
        continue
    for problem_dir in listdir(projEulerPath + '/' + contest_dir):
        # problem_dir = A, B, C, D ....
        if problem_dir == '.DS_Store':
            continue
        java_solutions = []
        python_solutions = []
        for solution in listdir(projEulerPath + '/' + contest_dir + '/' + problem_dir):
            # solution = 2736192.java ....
            if solution == '.DS_Store':
                continue
            solution_path = projEulerPath + '/' + contest_dir + '/' + problem_dir + '/' + solution
            submission_id = solution.split('.')[0]
            submission_id = ''.join(list(filter(str.isdigit, submission_id)))  # extract only digits
            ext = solution.split('.')[1]

            LibraryFuncs_str = ""

            if ext == 'java':
                print(contest_dir + '_' + problem_dir + '_' + ext)
                codeToWrite = None
                code = None
                with open(solution_path, 'r', encoding='utf8') as f:
                    code = f.read()

                LibraryFuncs_used = list(set(re.findall(r'Library(.*?)\(', code)))
                LibraryFuncs_used = [x.strip('.') for x in LibraryFuncs_used]
                for lib in LibraryFuncs_used:
                    LibraryFuncs_used.extend(javaLibDependencies[lib])
                LibraryFuncs_used = list(set(LibraryFuncs_used))

                print ("\t", "LibraryFuncs_used:", LibraryFuncs_used)

                flag_BigInt = False

                print (len(LibraryFuncs_used))
                if (len(LibraryFuncs_used) != 0):
                    libFuncs = []
                    LibraryFuncs_str = "\n" + "final class Library {\n"
                    for f in LibraryFuncs_used:
                        regexStr = "\n(.*?public.static.*?" + f.strip('.') + "\([\S\n\t\v ]*?})\n\t\n\t\n"
                        libFuncs.extend(re.findall(regexStr, Library_fileStr))

                    for libFunc in libFuncs:
                        LibraryFuncs_str += libFunc + "\n\n"                    
                            
                    if ("sqrt" in LibraryFuncs_used) or ("factorial" in LibraryFuncs_used) or ("binomial" in LibraryFuncs_used):
                        flag_BigInt = True


                    LibraryFuncs_str += "}\n"

                if "new Fraction" in code:
                    print ("\t", "new Fraction used")
                    print ("\t" + re.findall(r'(final.class.Fraction[\S\n\t\v ]*})', 
                                                            Library_fileStr)[0])
                    LibraryFuncs_str += "\n" + re.findall(r'(final.class.Fraction[\S\n\t\v ]*})', 
                                                            Library_fileStr)[0] + "\n"

                codeStrtIndx = code.index("\n\npublic final class p")
                if flag_BigInt and "import java.math.BigInteger" not in code:
                    code = code[:codeStrtIndx] + "\nimport java.math.BigInteger;\n" + code[codeStrtIndx:]
                    print ("=========================================================================")
                codeStrtIndx = code.index("\n\npublic final class p")
                print ("\t", codeStrtIndx, LibraryFuncs_str)
                code = code[:codeStrtIndx] + LibraryFuncs_str + code[codeStrtIndx:]

                code = code.replace("public final class p", "public class p")
                codeToWrite = code.replace("implements EulerSolution", "")

                with open(solution_path, 'w', encoding='utf8') as f:
                    f.write(codeToWrite)
                    
            elif ext == 'py':
                print(contest_dir + '_' + problem_dir + '_' + ext)
                with open(solution_path, 'r', encoding='utf8') as f:
                    code = f.read()

                LibraryFuncs_used = list(set(re.findall(r'eulerlib\.(.+?)[\(|\,]', code)))
                LibraryFuncs_used = [x.strip('.') for x in LibraryFuncs_used]

                print (LibraryFuncs_used)

                for lib in LibraryFuncs_used:
                    LibraryFuncs_used.extend(pythonLibDependencies[lib])
                LibraryFuncs_used = list(set(LibraryFuncs_used))

                print ("\t", "LibraryFuncs_used:", LibraryFuncs_used)

                inclStr = ""

                if "next_permutation" in LibraryFuncs_used:
                    inclStr += "E = TypeVar(\"E\", bound=\"_Comparable\")\n\n"
                    inclStr += "class _Comparable(Protocol):\n"
                    inclStr += "\tdef __lt__(self: E, other: E) -> bool: ...\n"
                    inclStr += "\tdef __le__(self: E, other: E) -> bool: ..."
                    inclStr += "\tdef __gt__(self: E, other: E) -> bool: ..."
                    inclStr += "\tdef __ge__(self: E, other: E) -> bool: ...\n"

                importStr = ""

                if (len(LibraryFuncs_used) != 0):
                    if len(list(set(re.findall(r'(import.*?math)', code)))) == 0:
                        if (len(list(set(re.findall(r'(import.*?array)', code))))) == 0 and \
                                        ("prime_generator" in LibraryFuncs_used):
                            importStr += "import math, array\n"
                        else:
                            importStr += "import math\n"
                    importStr += "from typing import Any, Callable, Dict, Generator, Generic, List, Optional, Protocol, TypeVar, cast\n"
                    libFuncs = []
                    LibraryFuncs_str = "\n" + "class eulerlib:\n"
                    for f in LibraryFuncs_used:
                        regexStr = "\n(def.*?" + f.strip('.') + "\([\S\n\t\v ]*?)\n\n\n"
                        print (regexStr)
                        funcStr = re.findall(regexStr, eulerlib_fileStr)[0]
                        funcStr = funcStr.replace("\n", "\n\t")
                        funcStr = "\t" + funcStr.strip()
                        funcStr = funcStr.replace("def " + f, "def xxyyxx")
                        for fWithin in LibraryFuncs_used:
                            if fWithin + "(" in funcStr:
                                funcStr = funcStr.replace(fWithin + "(", "eulerlib." + fWithin + "(")
                        funcStr = funcStr.replace("def xxyyxx", "def " + f)
                        libFuncs.append(funcStr)

                    for libFunc in libFuncs:
                        LibraryFuncs_str += libFunc + "\n\n"                    

                    LibraryFuncs_str += "\n"

                code = code.replace("eulerlib, ", "")
                code = code.replace("eulerlib,", "")
                code = code.replace("import eulerlib", "")
                code = code.replace(", eulerlib\n", "")
                code = code.replace(",eulerlib\n", "")

                codeStrtIndx = code.index("\n\n\n") + 1
                code = code[:codeStrtIndx] + importStr + "\n" + code[codeStrtIndx:]

                codeStrtIndx = code.index("\n\n\n") + 1
                print ("\t", codeStrtIndx, LibraryFuncs_str)
                codeToWrite = code[:codeStrtIndx] + LibraryFuncs_str + code[codeStrtIndx:]

                with open(solution_path, 'w', encoding='utf8') as f:
                    f.write(codeToWrite)

