import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def binomialCoeff(n, k):
        C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            j = 0
            while j <= min(i, k):
                if j == 0 or j == i:
                    C [i][j] = 1
                else:
                    C [i][j] = C [i - 1][j - 1] + C [i - 1][j]
                j += 1
        return C [n][k]
    @staticmethod
    def maxcoefficientvalue(n):
        if math.fmod(n, 2) == 0:
            return GFG.binomialCoeff(n, math.trunc(n / float(2)))
        else:
            return GFG.binomialCoeff(n, math.trunc((n + 1) / float(2)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print(GFG.maxcoefficientvalue(n))
