import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def binomialCoeff(n, k):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(0, k):
            res *= (n - i)
            res = math.trunc(res / float(i + 1))
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def catalan(n):
        c = GFG.binomialCoeff(2 * n, n)
        return math.trunc(c / float(n + 1))
    @staticmethod
    def findWays(n):
        if (n & 1) != 0:
            return 0
        return GFG.catalan(math.trunc(n / float(2)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        print("Total possible expressions of length " + str(n) + " is " + str(GFG.findWays(6)))
