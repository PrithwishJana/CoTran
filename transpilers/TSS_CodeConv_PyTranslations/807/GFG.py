import math

class GFG:
    @staticmethod
    def sumPowersK(n, k):
        sum = 0
        num = 1
        while num <= n:
            sum += num
            num *= k
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getSum(n, k):
        pwrK = GFG.sumPowersK(n, k)
        sumAll = math.trunc((n * (n + 1)) / float(2))
        return (sumAll - pwrK)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        k = 3
        print(GFG.getSum(n, k))
