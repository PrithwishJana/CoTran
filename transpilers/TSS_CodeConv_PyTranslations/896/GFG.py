import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nCr(n, r):
        fac = [0 for _ in range(100)]
        for i in range(0, n):
            fac [i] = 1
        i = 1
        while i < n + 1:
            fac [i] = fac [i - 1] * i
            i += 1
        ans = math.trunc(fac [n] / float(fac [n - r] * fac [r]))
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        k = 3
        ans = GFG.nCr(n + k - 1, k) + GFG.nCr(k - 1, n - 1)
        print(ans)
