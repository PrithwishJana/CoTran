import math

class GFG:
    @staticmethod
    def sumOfDigit(n, b):
        unitDigit = 0
        sum = 0
        while n > 0:
            unitDigit = math.fmod(n, b)
            sum += unitDigit
            n = math.trunc(n / float(b))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 50
        b = 2
        print(GFG.sumOfDigit(n, b), end = '')
