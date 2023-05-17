import math

class GFG:
    @staticmethod
    def Divisors(x):
        c = 0
        v = []
        while math.fmod(x, 2) == 0:
            c += 1
            x = math.trunc(x / float(2))
        v.append(c)
        c = 0
        while math.fmod(x, 3) == 0:
            c += 1
            x = math.trunc(x / float(3))
        v.append(c)
        c = 0
        while math.fmod(x, 7) == 0:
            c += 1
            x = math.trunc(x / float(7))
        v.append(c)
        v.append(x)
        return v
    @staticmethod
    def MinOperations(a, b):
        va = GFG.Divisors(a)
        vb = GFG.Divisors(b)
        if va[3] is not vb[3]:
            return - 1
        minOperations = abs(va[0] - vb[0]) + abs(va[1] - vb[1]) + abs(va[2] - vb[2])
        return minOperations
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 14
        b = 28
        print(GFG.MinOperations(a, b))
