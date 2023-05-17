import math

class Solution:
    @staticmethod
    def power(x, y, p):
        res = 1
        x = math.fmod(x, p)
        while y > 0:
            if (y & 1) != 0:
                res = math.fmod((res * x), p)
            y = y >> 1
            x = math.fmod((x * x), p)
        return res
    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        return Solution.gcd(math.fmod(b, a), a)
    @staticmethod
    def powerGCD(a, b, n):
        e = Solution.power(a, n, b)
        return Solution.gcd(e, b)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 5
        b = 4
        n = 2
        print(Solution.powerGCD(a, b, n), end = '')
