import math

class GFG:
    MAX = 100
    @staticmethod
    def recur(ind, cnt, last, a, n, k, dp):
        if cnt == k:
            return 0
        if ind == n:
            return (int) - 1e9
        if dp [ind][cnt] != - 1:
            return dp [ind][cnt]
        ans = 0
        for i in range(ind, n):
            if math.fmod(cnt, 2) == 0:
                ans = max(ans, GFG.recur(i + 1, cnt + 1, i, a, n, k, dp))
            else:
                ans = max(ans, GFG.__gcd(a [last], a [i]) + GFG.recur(i + 1, cnt + 1, 0, a, n, k, dp))
        return dp [ind][cnt] = ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if b == 0:
            return a
        return GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [4, 5, 3, 7, 8, 10, 9, 8]
        n = len(a)
        k = 4
        dp = [[0 for _ in range(GFG.MAX)] for _ in range(n)]
        for i in range(0, n):
            j = 0
            while j < GFG.MAX:
                dp [i][j] = - 1
                j += 1
        print(GFG.recur(0, 0, 0, a, n, k, dp))
