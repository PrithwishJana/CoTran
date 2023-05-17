import math

class GFG:
    @staticmethod
    def maxProd(N):
        if N == 0:
            return 1
        if N < 10:
            return N
        return max(GFG.maxProd(math.trunc(N / float(10))) * (math.fmod(N, 10)), GFG.maxProd(math.trunc(N / float(10)) - 1) * 9)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 390
        print(GFG.maxProd(N))
