import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        target = 93
        arr = [1, 31, 3, 1, 93, 3, 31, 1, 93]
        length = len(arr)
        totalCount = 0
        i = 0
        while i < length - 2:
            if math.fmod(target, arr [i]) == 0:
                j = i + 1
                while j < length - 1:
                    if math.fmod(target, (arr [i] * arr [j])) == 0:
                        toFind = math.trunc(target / float(arr [i] * arr [j]))
                        for k in range(j + 1, length):
                            if arr [k] == toFind:
                                totalCount += 1
                    j += 1
            i += 1
        print("Total number of triplets found: " + str(totalCount))
