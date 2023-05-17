import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isDivisible(n):
        d = 0
        while (math.trunc(n / float(100))) <= 0:
            d = math.fmod(n, 10)
            n = math.trunc(n / float(10))
            n = abs(n - (d * 7))
        return (math.fmod(n, 71) == 0)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 5041
        if GFG.isDivisible(N):
            print("Yes")
        else:
            print("No")
