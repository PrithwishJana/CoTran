import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if a == 0 or b == 0:
            return 0
        if a == b:
            return a
        if a > b:
            return GFG.__gcd(a - b, b)
        return GFG.__gcd(a, b - a)
    @staticmethod
    def NumberOfSquares(x, y):
        s = GFG.__gcd(x, y)
        ans = math.trunc((x * y) / float(s * s))
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        m = 385
        n = 60
        print(GFG.NumberOfSquares(m, n))
