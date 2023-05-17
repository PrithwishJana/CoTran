import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def seriesSum(n):
        sum = 0
        for i in range(1, n + 1):
            sum += math.trunc(i * (i + 1) / float(2))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print(GFG.seriesSum(n))
