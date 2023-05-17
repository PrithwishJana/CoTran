import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
    def sameRemainder(a, b, c):
        a1 = (b - a)
        b1 = (c - b)
        c1 = (c - a)
        return GFG.gcd(a1, GFG.gcd(b1, c1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 62
        b = 132
        c = 237
        print(GFG.sameRemainder(a, b, c))
