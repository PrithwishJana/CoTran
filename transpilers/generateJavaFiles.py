from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE
import shutil, time, random, os

currPath = "../AVATAR_data/"
root_folder = currPath + "third_party"
print (root_folder)
extJavaLibraries = currPath + "data_extLibraries/"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)


def generateJavaFiles(javaPrograms):
    global extJavaLibraries
    folderNm = "./javaFiles"
    for indx, oneLineProg in enumerate(javaPrograms):
        folderNmNew = os.path.join(folderNm, str(indx))
        os.makedirs(folderNmNew)
        public_class_name = 'Main'
        if "public class" in oneLineProg:
            tokens = oneLineProg.split("public class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]
        elif "public final class" in oneLineProg:
            tokens = oneLineProg.split("public final class", 1)
            if len(tokens) == 2 and len(tokens[1]) > 0:
                public_class_name = tokens[1].split()[0]
        filename = os.path.join(folderNmNew, '{}.java'.format(public_class_name))
        program = jprocessor.detokenize_code(oneLineProg)
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)
    


#main
javaPath = "../AVATAR_data/data_LARGE/test.java-python.java"

programs = []
with open(javaPath, encoding='utf8') as f:
    for line in f:
        programs.append(line.strip())

generateJavaFiles(programs)