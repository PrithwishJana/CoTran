import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNthTerm(N):
        ans = 0
        if math.fmod(N, 2) == 0:
            ans = (math.trunc(N / float(2))) * 6 + (math.trunc(N / float(2))) * 2
        else:
            ans = (math.trunc(N / float(2)) + 1) * 6 + (math.trunc(N / float(2))) * 2
        print(str(ans) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        GFG.findNthTerm(N)
