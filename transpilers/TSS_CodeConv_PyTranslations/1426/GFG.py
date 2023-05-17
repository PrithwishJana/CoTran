import math

class GFG:
    @staticmethod
    def sn(n, an):
        return math.trunc((n * (1 + an)) / float(2))
    @staticmethod
    def trace(n, m):
        an = 1 + (n - 1) * (m + 1)
        rowmajorSum = GFG.sn(n, an)
        an = 1 + (n - 1) * (n + 1)
        colmajorSum = GFG.sn(n, an)
        return rowmajorSum + colmajorSum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        M = 3
        print(GFG.trace(N, M))
