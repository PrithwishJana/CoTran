import math

class GFG:
    @staticmethod
    def possibleways(n):
        if math.fmod(n, 2) == 1:
            return 0
        elif math.fmod(n, 4) == 0:
            return math.trunc(n / float(4)) - 1
        else:
            return math.trunc(n / float(4))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 20
        print(GFG.possibleways(n))
