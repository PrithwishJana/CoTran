import math

class GFG:
    MOD = 1000000007
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fact(n):
        res = 1
        for i in range(2, n + 1):
            res = res * i
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nCr(n, r):
        return math.trunc(GFG.fact(n) / float(GFG.fact(r) * GFG.fact(n - r)))
    @staticmethod
    def powmod(a, n):
        if n == 0:
            return 1
        pt = GFG.powmod(a, math.trunc(n / float(2)))
        pt = math.fmod((pt * pt), GFG.MOD)
        if math.fmod(n, 2) == 1:
            return math.fmod((pt * a), GFG.MOD)
        else:
            return pt
    @staticmethod
    def CountSubset(arr, n):
        ans = GFG.powmod(2, n - 1)
        Arrays.sort(arr)
        for i in range(0, n):
            j = i + 1
            while j < n and arr [j] == arr [i]:
                r = n - 1 - j
                l = i
                ans = math.fmod((ans + GFG.nCr(l + r, l)), GFG.MOD)
                j += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 2]
        n = len(arr)
        print(GFG.CountSubset(arr, n))
