import math

class GFG:
    @staticmethod
    def ncr(n, r):
        ans = 1
        for i in range(1, r + 1):
            ans *= (n - r + i)
            ans = math.trunc(ans / float(i))
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def totalWays(X, Y, M, W):
        return (GFG.ncr(M, X) * GFG.ncr(W, Y))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        X = 4
        Y = 3
        M = 6
        W = 5
        print(GFG.totalWays(X, Y, M, W))
