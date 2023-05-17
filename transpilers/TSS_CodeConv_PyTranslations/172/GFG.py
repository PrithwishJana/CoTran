import math

class GFG:
    v = []
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def multiply(x):
        carry = 0
        size = len(GFG.v)
        for i in range(0, size):
            res = carry + GFG.v[i] * x
            GFG.v[i] = math.fmod(res, 10)
            carry = math.trunc(res / float(10))
        while carry != 0:
            GFG.v.append(math.fmod(carry, 10))
            carry = math.trunc(carry / float(10))
    @staticmethod
    def findSumOfDigits(n):
        GFG.v.append(1)
        for i in range(1, n + 1):
            GFG.multiply(i)
        sum = 0
        size = len(GFG.v)
        for i in range(0, size):
            sum += GFG.v[i]
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 1000
        print(GFG.findSumOfDigits(n))
