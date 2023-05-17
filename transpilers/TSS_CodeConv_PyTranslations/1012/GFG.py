import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculate(a, b, n, m):
        mul = 1
        for i in range(0, m):
            if b [i] != 0:
                mul = mul * b [i]
        for i in range(0, n):
            x = int(math.floor(math.trunc(a [i] / float(mul))))
            print(str(x) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [5, 100, 8]
        b = [2, 3]
        n = len(a)
        m = len(b)
        GFG.calculate(a, b, n, m)
