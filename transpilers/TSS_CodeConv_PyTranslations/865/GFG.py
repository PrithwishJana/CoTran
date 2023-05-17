import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPossible(x, y, z):
        a = x * x + y * y + z * z
        if math.ceil(a) == 1 and math.floor(a) == 1:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 0.70710678f
        m = 0.5f
        n = 0.5f
        if GFG.isPossible(l, m, n):
            print("Yes")
        else:
            print("No")
