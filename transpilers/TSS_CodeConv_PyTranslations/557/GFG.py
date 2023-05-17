import math

class GFG:
    @staticmethod
    def xorCalc(k):
        if k == 1:
            return 2
        if ((k + 1) & k) == 0:
            return math.trunc(k / float(2))
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 31
        print(GFG.xorCalc(k))
