correctionFiles = ["corr-valid.java-python.java", "corr-valid.java-python.python", 
            "corr-test.java-python.java", "corr-test.java-python.python",
            "corr-train.java-python.java", "corr-train.java-python.python"]

downloadedFiles = ["dwnlded-valid.java-python.java", "dwnlded-valid.java-python.python", 
            "dwnlded-test.java-python.java", "dwnlded-test.java-python.python",
            "dwnlded-train.java-python.java", "dwnlded-train.java-python.python"]

newCorrectedFiles = ["../" + x.lstrip("dwnlded-") for x in downloadedFiles]

for fIdx, f in enumerate(correctionFiles):
    print ("\n\n", f, "\n\n")
    with open(downloadedFiles[fIdx]) as file:
        downloadedCodes = [line.strip() for line in file]
    with open(f) as file:
        correctedCodes = [line.strip() for line in file]
    count = 0
    newCorrectedCodes = []
    for dwnldIndx, dwnldCode in enumerate(downloadedCodes):
        correctedCode = correctedCodes[dwnldIndx]
        if len(correctedCode) != 0:
            newCorrectedCodes.append(correctedCode + "\n")
            count += 1
        else:
            newCorrectedCodes.append(dwnldCode + "\n")

    newCorrectedCodes[-1] = newCorrectedCodes[-1].rstrip()
    print (newCorrectedFiles[fIdx])
    ff = open(newCorrectedFiles[fIdx], "w")
    ff.writelines(newCorrectedCodes)
    ff.close()
    print (count)
