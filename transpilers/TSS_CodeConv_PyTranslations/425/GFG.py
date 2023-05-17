import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculateSum(n, k):
        res = 1
        MOD = 1000000007
        for i in range(0, k):
            res = math.fmod((res * n), MOD)
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        k = 3
        print(GFG.calculateSum(n, k), end = '')
