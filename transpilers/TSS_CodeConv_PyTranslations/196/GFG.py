import math

class GFG:
    MAXN = 1000005
    even = [0 for _ in range(MAXN)]
    odd = [0 for _ in range(MAXN)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def precompute(arr, n):
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 1:
                GFG.odd [i] = 1
            if math.fmod(arr [i], 2) == 0:
                GFG.even [i] = 1
        for i in range(1, n):
            GFG.even [i] = GFG.even [i] + GFG.even [i - 1]
            GFG.odd [i] = GFG.odd [i] + GFG.odd [i - 1]
    @staticmethod
    def isOdd(L, R):
        cnt = GFG.odd [R]
        if L > 0:
            cnt -= GFG.odd [L - 1]
        if cnt == R - L + 1:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def performQueries(a, n, q, m):
        GFG.precompute(a, n)
        for i in range(0, m):
            L = q [i][0]
            R = q [i][1]
            if GFG.isOdd(L, R):
                print("Odd")
            else:
                print("Even")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 1, 5, 7, 6, 8, 9]
        n = len(a)
        q = [[ 0, 2 ], [ 1, 2 ], [ 2, 3 ], [ 3, 6 ]]
        m = len(q)
        GFG.performQueries(a, n, q, m)
