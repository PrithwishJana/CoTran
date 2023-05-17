import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getSum(n):
        sum = 0
        while n != 0:
            sum = sum + math.fmod(n, 10)
            n = math.trunc(n / float(10))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 687
        print(GFG.getSum(n))
