import math

class GFG:
    @staticmethod
    def cntWays(n):
        if math.fmod(n, 2) == 1:
            return 0
        else:
            return math.trunc((n - 2) / float(4))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 18
        print(GFG.cntWays(n))
