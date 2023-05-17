import math

class GFG:
    @staticmethod
    def findNature(a, b, n):
        if n == 0:
            return True if (a & 1) == 1 else False
        if n == 1:
            return True if (b & 1) == 1 else False
        if (a & 1) == 0:
            if (b & 1) == 0:
                return False
            else:
                return (math.fmod(n, 3) != 0)
        else:
            if (b & 1) == 0:
                return (math.fmod((n - 1), 3) != 0)
            else:
                return (math.fmod((n + 1), 3) != 0)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 4
        n = 3
        if GFG.findNature(a, b, n):
            print("Odd")
        else:
            print("Even")
