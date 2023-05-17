import os
from pathlib import Path
from codegen.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen.preprocessing.lang_processors.python_processor import PythonProcessor
root_folder = "../AVATAR_data/third_party"
jprocessor = JavaProcessor(root_folder=root_folder)
pyprocessor = PythonProcessor(root_folder=root_folder)

finalList = []

for i in range(0,1746):
    fold = os.path.join("./py2java_javaTranslations", str(i))
    all_files = os.listdir(fold)
    print (fold, all_files)
    if len(all_files) != 1:
        print ("SKIP---------")
        oneLineCodeJv = "3 = i"
        finalList.append(oneLineCodeJv + "\n")
        continue
    txt = Path(os.path.join("./py2java_javaTranslations", str(i), all_files[0])).read_text()
    try:
        oneLineCodeJv = " ".join(jprocessor.tokenize_code(txt))
    except:
        oneLineCodeJv = "3 = i"
    finalList.append(oneLineCodeJv + "\n")

f = open("py2java_java.out", "a")
f.writelines(finalList)
f.close()
