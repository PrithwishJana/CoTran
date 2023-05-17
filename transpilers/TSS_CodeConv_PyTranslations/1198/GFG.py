import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPerfectSquare(x):
        sr = int(math.sqrt(x))
        if sr * sr == x:
            print("Yes")
        else:
            print("No")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        k = 2
        GFG.isPerfectSquare(n + k)
