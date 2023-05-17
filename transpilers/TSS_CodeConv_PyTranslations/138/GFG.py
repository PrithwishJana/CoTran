import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNthTerm(n):
        if math.fmod(n, 2) == 0:
            n = math.trunc(n / float(2))
            print(int(3) ** (n - 1) + "\n", end = '')
        else:
            n = (math.trunc(n / float(2))) + 1
            print(int(2) ** (n - 1) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 4
        GFG.findNthTerm(N)
        N = 11
        GFG.findNthTerm(N)
