import math

class GFG:
    @staticmethod
    def cone(a):
        if a < 0:
            return - 1
        r = float((a * math.sqrt(2))) / 3
        h = (2 * a) / 3
        V = float((3.14 * r ** 2 * h))
        return V
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 5
        print("{0:.4f}".format(GFG.cone(a)))
