import math

class GFG:
    N = 10000
    MOD = 1000000007
    F = [0 for _ in range(N)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def precompute():
        GFG.F [1] = 2
        GFG.F [2] = 3
        GFG.F [3] = 4
        i = 4
        while i < GFG.N:
            GFG.F [i] = math.fmod((GFG.F [i - 1] + GFG.F [i - 2]), GFG.MOD)
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 8
        GFG.precompute()
        print(GFG.F [n])
