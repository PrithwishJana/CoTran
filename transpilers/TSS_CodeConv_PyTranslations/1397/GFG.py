import math

class GFG:
    N = 100005
    d = [0 for _ in range(N)]
    pre = [0 for _ in range(N)]
    @staticmethod
    def Positive_Divisors():
        i = 1
        while i < GFG.N:
            j = 1
            while j * j <= i:
                if math.fmod(i, j) == 0:
                    if j * j == i:
                        GFG.d [i] += 1
                    else:
                        GFG.d [i] += 2
                j += 1
            i += 1
        ans = 0
        i = 2
        while i < GFG.N:
            if GFG.d [i] == GFG.d [i - 1]:
                ans += 1
            GFG.pre [i] = ans
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.Positive_Divisors()
        n = 15
        print(GFG.pre [n])
