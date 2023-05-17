import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(n):
        sum = 0
        for i in range(1, n + 1):
            sum += (math.trunc((i * (i + 1) * (2 * i + 1)) / float(6)))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.findSum(n))
