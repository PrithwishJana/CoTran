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
    def largestDigitSumdivisior(n):
        res = 0
        i = 1
        while i <= math.sqrt(n):
            if math.fmod(n, i) == 0:
                res = max(res, GFG.getSum(i))
                res = max(res, GFG.getSum(math.trunc(n / float(i))))
            i += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 14
        print(GFG.largestDigitSumdivisior(n))
