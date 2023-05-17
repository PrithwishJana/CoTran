import math

class GFG:
    def getMinNum(self, a, b, c):
        if c < a or c > b:
            return c
        x = ((math.trunc(b / float(c))) * c) + c
        return x
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 4
        c = 4
        g = GFG()
        print(g.getMinNum(a, b, c))
