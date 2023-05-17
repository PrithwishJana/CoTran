import math

class GFG:
    @staticmethod
    def minimumNumbers(n, s):
        if (math.fmod(s, n)) > 0:
            return math.trunc(s / float(n)) + 1
        else:
            return math.trunc(s / float(n))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        s = 11
        print(GFG.minimumNumbers(n, s))
