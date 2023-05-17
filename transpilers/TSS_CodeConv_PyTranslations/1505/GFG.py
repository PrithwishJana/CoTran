import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(n):
        return math.trunc((n * (n + 1) * (n + 1) * (n + 2)) / float(12))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.findSum(n))
