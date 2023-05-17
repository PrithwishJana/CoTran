import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def power(x, y, p):
        res = 1
        x = math.fmod(x, p)
        while y > 0:
            if math.fmod(y, 2) == 1:
                res = math.fmod((res * x), p)
            y = y >> 1
            x = math.fmod((x * x), p)
        return res
    @staticmethod
    def findModuloByM(X, N, M):
        if N < 6:
            temp = ""
            for i in range(0, N):
                temp = temp + chr((X + 48))
            res = math.fmod(int(temp), M)
            return res
        if math.fmod(N, 2) == 0:
            half = math.fmod(GFG.findModuloByM(X, math.trunc(N / float(2)), M), M)
            res = math.fmod((half * GFG.power(10, math.trunc(N / float(2)), M) + half), M)
            return res
        else:
            half = math.fmod(GFG.findModuloByM(X, math.trunc(N / float(2)), M), M)
            res = math.fmod((half * GFG.power(10, math.trunc(N / float(2)) + 1, M) + half * 10 + X), M)
            return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        X = 6
        N = 14
        M = 9
        print(GFG.findModuloByM(X, N, M))
