import math

class GFG:
    @staticmethod
    def digSum(n):
        sum = 0
        rem = 0
        while n > 0:
            rem = math.fmod(n, 10)
            sum += rem
            n = math.trunc(n / float(10))
        return sum
    @staticmethod
    def findX(n):
        for i in range(0, n + 1):
            if i + GFG.digSum(i) == n:
                return i
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 43
        print("x = " + str(GFG.findX(n)))
