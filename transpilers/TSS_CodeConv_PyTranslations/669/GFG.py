import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        while b != 0:
            t = b
            b = math.fmod(a, b)
            a = t
        return a
    @staticmethod
    def findMinDiff(a, b, x, y):
        g = GFG.gcd(a, b)
        diff = math.fmod(abs(x - y), g)
        return min(diff, g - diff)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 20
        b = 52
        x = 5
        y = 7
        print(GFG.findMinDiff(a, b, x, y))
