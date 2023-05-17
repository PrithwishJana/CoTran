import math

class GFG:
    @staticmethod
    def normal(m, n):
        N = float(((abs(m) * abs(n)) / math.sqrt((abs(m) * abs(m)) + (abs(n) * abs(n)))))
        return N
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        m = - 5
        n = 3
        print(GFG.normal(m, n))
