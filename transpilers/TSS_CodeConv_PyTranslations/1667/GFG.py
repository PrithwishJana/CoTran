import math

class GFG:
    @staticmethod
    def moduloMultiplication(a, b, mod):
        res = 0
        a = math.fmod(a, mod)
        while b > 0:
            if (b & 1) > 0:
                res = math.fmod((res + a), mod)
            a = math.fmod((2 * a), mod)
            b >>= 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 10123465234878998
        b = 65746311545646431
        m = 10005412336548794
        print(GFG.moduloMultiplication(a, b, m), end = '')
