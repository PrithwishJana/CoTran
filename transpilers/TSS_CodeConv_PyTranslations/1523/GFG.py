import math

class GFG:
    @staticmethod
    def findDelta(a, b, c, d):
        return math.trunc((b * c - a * d) / float(d - c))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 3
        b = 9
        c = 3
        d = 5
        print("\u0394X = " + str(GFG.findDelta(a, b, c, d)), end = '')
