# STEP 1: Create out_j.txt : python check_runtimeOutput.py --input_file train.java-python.java --id_file ../train.java-python.id --language java --writeDir ./junk > out_j.txt 2>&1 
# STEP 2: Create out_py.txt : python check_runtimeOutput.py --input_file train.java-python.python --id_file ../train.java-python.id --language python --writeDir ./junk > out_py.txt 2>&1 
# STEP 3: Run this script: python parse_out.py

from difflib import SequenceMatcher
import time

def all_err(lines):
    flag = 0
    flag2 = None
    outs = []
    console = []
    linenums = []

    o, c = "", ""
    lineNum = None

    for line in lines:
        if flag == 1 and ((line == "\n" and flag2 == "o") or "MATCH" in line):
            flag = 0
            if "MATCH" in line:
                o = o.replace(" ", "")
                c = c.replace(" ", "")
                if "DIDN'T MATCH" in line:
                    linenums.append(lineNum)
                    outs.append(o)
                    console.append(c)
                else:
                    pass
                    # assert o == c, f"o != c for {o} and {c}"
                o, c = "", ""
                lineNum = None
        
        if flag == 1:
            if flag2 == "o":
                o += line.strip()
            if flag2 == "c":
                c += line.strip()

        if "---> outputs:" in line:
            flag2 = "o"
            flag = 1
        if "---> console_out" in line:
            flag2 = "c"
            flag = 1
        
        if "---> lineNum:" in line:
            lineNum = line.split(":")[1].strip()

    return outs, console, linenums

f = open("out_py.txt", "r")
lines = f.readlines()
f.close()

outs_p, console_p, linenums_p = all_err(lines)
print("Python: ", len(linenums_p))

f = open("out_j.txt", "r")
lines = f.readlines()
f.close()

outs_j, console_j, linenums_j = all_err(lines)
print("Java: ", len(linenums_j))

linenums_ps = set(linenums_p)
linenums_js = set(linenums_j)
intersection_ = linenums_ps.intersection(linenums_js)
print("Intersection: ", len(intersection_))#, intersection_)
# print("Python - Intersection: ", len(linenums_ps - intersection_), linenums_ps - intersection_)
# print("Java - Intersection: ", len(linenums_js - intersection_), linenums_js - intersection_)

same_console = 0
crashes = 0
all_ratios = []

# compare outputs of the intersection
for l in intersection_:
    py_console = console_p[linenums_p.index(l)]
    j_console = console_j[linenums_j.index(l)]
    out_py = outs_p[linenums_p.index(l)]
    if len(py_console) == 0 or len(j_console) == 0:
        crashes += 1
    elif py_console == j_console:
        same_console += 1
        print("Line no.:", l)
        print("Python console:")
        print(py_console)
    else:
        s = SequenceMatcher(None, py_console, j_console) # difference between the two outputs
        all_ratios.append(s.ratio())

print("Same outputs: ", same_console, " out of ", len(intersection_))
print("Crashes: ", crashes, " out of ", len(intersection_))

import matplotlib.pyplot as plt
import numpy as np

bp = plt.boxplot(all_ratios)
 
# show plot
plt.savefig('boxplot.png')

print("Mean: ", np.mean(all_ratios))
print("Max: ", np.max(all_ratios))
print("Greater than 0.9: ", len([x for x in all_ratios if x > 0.9]))
print("Greater than 0.95: ", len([x for x in all_ratios if x > 0.95]))
