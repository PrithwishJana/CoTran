import math

class GFG:
    @staticmethod
    def inv(a, m):
        m0 = m
        t = 0
        q = 0
        x0 = 0
        x1 = 1
        if m == 1:
            return 0
        while a > 1:
            q = math.trunc(a / float(m))
            t = m
            m = math.fmod(a, m)
            a = t
            t = x0
            x0 = x1 - q * x0
            x1 = t
        if x1 < 0:
            x1 += m0
        return x1
    @staticmethod
    def findMinX(num, rem, k):
        prod = 1
        for i in range(0, k):
            prod *= num [i]
        result = 0
        for i in range(0, k):
            pp = math.trunc(prod / float(num [i]))
            result += rem [i] * GFG.inv(pp, num [i]) * pp
        return math.fmod(result, prod)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = [3, 4, 5]
        rem = [2, 3, 1]
        k = len(num)
        print("x is " + str(GFG.findMinX(num, rem, k)))
