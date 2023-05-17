import math

class GFG:
    @staticmethod
    def countNums(a, b, c, d):
        x = math.trunc(b / float(c)) - math.trunc((a - 1) / float(c))
        y = math.trunc(b / float(d)) - math.trunc((a - 1) / float(d))
        k = math.trunc((c * d) / float(GFG.__gcd(c, d)))
        z = math.trunc(b / float(k)) - math.trunc((a - 1) / float(k))
        return b - a + 1 - x - y + z
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if b == 0:
            return a
        return GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 10
        b = 50
        c = 4
        d = 6
        print(GFG.countNums(a, b, c, d))
