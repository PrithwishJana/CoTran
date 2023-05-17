import os, shutil

src = "/scratch/pjana/AVATAR_data/python/"
dest = "/scratch/pjana/AVATAR_data/ProjectEuler_ORIGNew/"

for file in os.listdir(src):
    print (file)
    if file.endswith(".py") and (file not in ["eulerlib.py", "eulertest.py"]):
        print(os.path.join(src, file))
        shutil.move(os.path.join(src, file), os.path.join(dest, file.split('.')[0], "A", "xx.py"))
        os.remove(os.path.join(dest, file.split('.')[0], "A", "2.py"))
        os.rename(os.path.join(dest, file.split('.')[0], "A", "xx.py"), os.path.join(dest, file.split('.')[0], "A", "2.py"))
        if os.path.exists(os.path.join(dest, file.split('.')[0], "xx.py")):
            os.remove(os.path.join(dest, file.split('.')[0], "xx.py"))