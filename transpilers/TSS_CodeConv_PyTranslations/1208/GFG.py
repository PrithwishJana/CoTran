import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fourthPowerSum(n):
        return math.trunc(((6 * n * n * n * n * n) + (15 * n * n * n * n) + (10 * n * n * n) - n) / float(30))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        print(GFG.fourthPowerSum(n))
