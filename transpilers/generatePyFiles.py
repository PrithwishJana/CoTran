from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
from subprocess import run, check_output, CalledProcessError, STDOUT, PIPE
import shutil, time, random, os

currPath = "../AVATAR_data/"
root_folder = currPath + "third_party"
print (root_folder)
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)


def generatePyFiles(pyPrograms):
    folderNm = "./pyFiles"
    for indx, oneLineProg in enumerate(pyPrograms):
        folderNmNew = os.path.join(folderNm, str(indx))
        os.makedirs(folderNmNew)

        program = pyprocessor.detokenize_code(oneLineProg)

        filename = os.path.join(folderNmNew, 'main.py')
        with open(filename, 'w', encoding='utf8') as fw:
            fw.write(program)
        print (indx)



#main
pyPath = "../AVATAR_data/data_LARGE/test.java-python.python"

programs = []
with open(pyPath, encoding='utf8') as f:
    for line in f:
        programs.append(line.strip())

generatePyFiles(programs)