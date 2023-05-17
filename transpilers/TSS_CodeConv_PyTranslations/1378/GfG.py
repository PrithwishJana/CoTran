import math

class GfG:
    @staticmethod
    def removeZero(n):
        res = 0
        d = 1
        while n > 0:
            if math.fmod(n, 10) != 0:
                res += (math.fmod(n, 10)) * d
                d *= 10
            n = math.trunc(n / float(10))
        return res
    @staticmethod
    def isEqual(a, b):
        if GfG.removeZero(a) + GfG.removeZero(b) == GfG.removeZero(a + b):
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 105
        b = 106
        if GfG.isEqual(a, b) == True:
            print("Yes")
        else:
            print("No")
