sources = ["aizu", "atcoder", "codeforces", "codejam", "geeksforgeeks", "leetcode", "projecteuler"]

errFiles = ["corr-valid.java-python.java", "corr-valid.java-python.python", 
            "corr-test.java-python.java", "corr-test.java-python.python",
            "corr-train.java-python.java", "corr-train.java-python.python"]

idFiles = ["../valid.java-python.id", "../valid.java-python.id", 
            "../test.java-python.id", "../test.java-python.id",
            "../train.java-python.id", "../train.java-python.id"]

for fIdx, f in enumerate(errFiles):
    print ("\n\n", f, "\n\n")
    with open(idFiles[fIdx]) as file:
        ids = [line.strip() for line in file]
    with open(f) as file:
        lines = [line.strip() for line in file]
    for source in sources:
        count = 0
        for errIndx, errFile in enumerate(errFiles):
            if len(errFile) != 0 and (source in ids[errIndx]):
                count += 1
        print (source, count)