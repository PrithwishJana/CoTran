import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(M, N, s):
        if math.fmod(N, s) == 0:
            N = math.trunc(N / float(s))
        else:
            N = (math.trunc(N / float(s))) + 1
        if math.fmod(M, s) == 0:
            M = math.trunc(M / float(s))
        else:
            M = (math.trunc(M / float(s))) + 1
        return M * N
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 12
        M = 13
        s = 4
        print(GFG.solve(M, N, s))
