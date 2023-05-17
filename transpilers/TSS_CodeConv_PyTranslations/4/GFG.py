import math

class GFG:
    @staticmethod
    def fastPow(N, K):
        if K == 0:
            return 1
        temp = GFG.fastPow(N, math.trunc(K / float(2)))
        if math.fmod(K, 2) == 0:
            return temp * temp
        else:
            return N * temp * temp
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(N, K):
        return K * GFG.fastPow(K - 1, N - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        K = 3
        print(GFG.countWays(N, K))
