import math

class GFG:
    @staticmethod
    def countIntersections(n):
        return math.trunc(n * (n - 1) / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.countIntersections(n))
