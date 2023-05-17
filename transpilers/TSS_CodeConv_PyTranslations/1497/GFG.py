import math

class GFG:
    @staticmethod
    def maxHandshake(n):
        return math.trunc((n * (n - 1)) / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        print(GFG.maxHandshake(n))
