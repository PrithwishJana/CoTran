import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return GFG.__gcd(a - b, b)
        return GFG.__gcd(a, b - a)
    @staticmethod
    def printRatio(a, b, c, d):
        if b * c > a * d:
            temp = c
            c = d
            d = c
            temp = a
            a = b
            b = temp
        lcm = math.trunc((a * c) / float(GFG.__gcd(a, c)))
        x = math.trunc(lcm / float(a))
        b *= x
        y = math.trunc(lcm / float(c))
        d *= y
        k = GFG.__gcd(b, d)
        b = math.trunc(b / float(k))
        d = math.trunc(d / float(k))
        print(str(b) + ":" + str(d), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 4
        b = 3
        c = 2
        d = 2
        GFG.printRatio(a, b, c, d)
