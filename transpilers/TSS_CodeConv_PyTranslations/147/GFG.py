import math

class GFG:
    @staticmethod
    def printCombination(n):
        for i in range(1, n):
            if math.fmod(i, 3) != 0:
                for j in range(1, n):
                    if math.fmod(j, 3) != 0:
                        for k in range(1, n):
                            if math.fmod(k, 3) != 0 and (i + j + k) == n:
                                print(str(i) + " " + str(j) + " " + str(k))
                                return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 233
        GFG.printCombination(n)
