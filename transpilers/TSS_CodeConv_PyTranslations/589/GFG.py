import math

class GFG:
    discard_count = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def power(a, n):
        if n == 0:
            return 1
        p = GFG.power(a, math.trunc(n / float(2)))
        p = p * p
        if math.fmod(n, 2) == 1:
            p = p * a
        return p
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(i, n, sum, k, a, prefix):
        if sum > k:
            GFG.discard_count += GFG.power(2, n - i)
            return
        if i == n:
            return
        rem = prefix [n - 1] - prefix [i]
        if sum + a [i] + rem > k:
            GFG.solve(i + 1, n, sum + a [i], k, a, prefix)
        if sum + rem > k:
            GFG.solve(i + 1, n, sum, k, a, prefix)
    @staticmethod
    def countSubsequences(arr, n, K):
        sum = 0.0f
        k = float(math.log(K))
        prefix = [0 for _ in range(n)]
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = float(math.log(arr [i]))
            sum += a [i]
        prefix [0] = a [0]
        for i in range(1, n):
            prefix [i] = prefix [i - 1] + a [i]
        total = GFG.power(2, n) - 1
        if sum <= k:
            return int(total)
        GFG.solve(0, n, 0.0f, k, a, prefix)
        return int((total - GFG.discard_count))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 8, 7, 2]
        n = len(arr)
        k = 50
        print(GFG.countSubsequences(arr, n, k), end = '')
