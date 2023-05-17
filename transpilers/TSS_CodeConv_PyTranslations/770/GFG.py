import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(n):
        n -= 1
        sum = 0
        sum += math.trunc((n * (n + 1)) / float(2))
        sum += math.trunc((n * (n + 1) * (2 * n + 1)) / float(6))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.findSum(n))
