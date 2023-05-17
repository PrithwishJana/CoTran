import math

class GFG:
    @staticmethod
    def SUM(n, m):
        if m == 1:
            return (math.trunc(n * (n + 1) / float(2)))
        sum = GFG.SUM(n, m - 1)
        return (math.trunc(sum * (sum + 1) / float(2)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        m = 3
        print("SUM(" + str(n) + ", " + str(m) + "): " + str(GFG.SUM(n, m)))
