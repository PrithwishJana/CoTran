import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def power(x, a):
        res = 1
        while a > 0:
            if (a & 1) > 0:
                res = res * x
            x = x * x
            a >>= 1
        return res
    @staticmethod
    def breakInteger(N):
        if N == 2:
            return 1
        if N == 3:
            return 2
        maxProduct = - 1
        if math.fmod(N, 3) == 0:
            maxProduct = GFG.power(3, math.trunc(N / float(3)))
        elif math.fmod(N, 3) == 1:
            maxProduct = 2 * 2 * GFG.power(3, (math.trunc(N / float(3))) - 1)
        elif math.fmod(N, 3) == 2:
            maxProduct = 2 * GFG.power(3, math.trunc(N / float(3)))
        return maxProduct
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        maxProduct = GFG.breakInteger(10)
        print(maxProduct)
