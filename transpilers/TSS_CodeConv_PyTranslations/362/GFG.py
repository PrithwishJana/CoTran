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
    def findValue(x, y, z):
        g = GFG.__gcd(y, z)
        return math.trunc((x * g) / float(GFG.__gcd(x, g)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 30
        y = 40
        z = 400
        print(GFG.findValue(x, y, z), end = '')
