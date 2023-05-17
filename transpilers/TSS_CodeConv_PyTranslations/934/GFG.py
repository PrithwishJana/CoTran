import math

class GFG:
    @staticmethod
    def sumAP(n, d):
        n = math.trunc(n / float(d))
        return math.trunc((n) * (1 + n) * d / float(2))
    @staticmethod
    def sumMultiples(n):
        n -= 1
        return GFG.sumAP(n, 2) + GFG.sumAP(n, 5) - GFG.sumAP(n, 10)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 20
        print(GFG.sumMultiples(n))
