import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(N):
        E = math.trunc((N * (N - 1)) / float(2))
        if N == 1:
            return 0
        return int(2) ** (E - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 4
        print(GFG.countWays(N))
