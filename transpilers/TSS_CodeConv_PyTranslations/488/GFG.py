import math

class GFG:
    c = [0 for _ in range(100)]
    @staticmethod
    def coef(n):
        GFG.c [0] = 1
        i = 0
        while i < n:
            GFG.c [1 + i] = 1
            for j in range(i, 0, -1):
                GFG.c [j] = GFG.c [j - 1] - GFG.c [j]
            GFG.c [0] = - GFG.c [0]
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        GFG.coef(n)
        GFG.c [0] += 1
        GFG.c [n] -= 1
        i = n
#JAVA TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by Java to Python Converter:
#ORIGINAL LINE: while ((i --) > 0 && c [i] % n == 0);
        while (i --) > 0 and math.fmod(GFG.c [i], n) == 0:
            pass
        return i < 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 37
        if GFG.isPrime(n):
            print("Prime")
        else:
            print("Not Prime")
