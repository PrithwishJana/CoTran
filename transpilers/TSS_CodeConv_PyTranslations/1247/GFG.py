import math

class GFG:
    @staticmethod
    def countDyckPaths(n):
        res = 1
        for i in range(0, n):
            res *= (2 * n - i)
            res = math.trunc(res / float(i + 1))
        return math.trunc(res / float(n + 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print("Number of Dyck Paths is " + str(GFG.countDyckPaths(n)))
