import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPerfectSquare(x):
        sr = math.sqrt(x)
        return ((sr - math.floor(sr)) == 0)
    @staticmethod
    def isSunnyNum(n):
        if GFG.isPerfectSquare(n + 1):
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        if GFG.isSunnyNum(n):
            print("Yes")
        else:
            print("No")
