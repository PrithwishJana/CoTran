import math

class GFG:
    maxn = 16
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def precompute():
        dp = [0 for _ in range(GFG.maxn)]
        arr = [4, 6, 9]
        i = 0
        while i < GFG.maxn:
            dp [i] = - 1
            i += 1
        dp [0] = 0
        i = 1
        while i < GFG.maxn:
            for k in range(0, 3):
                j = arr [k]
                if i >= j and dp [i - j] != - 1:
                    dp [i] = max(dp [i], dp [i - j] + 1)
            i += 1
        return dp
    @staticmethod
    def Maximum_Summands(dp, n):
        if n < GFG.maxn:
            return dp [n]
        else:
            t = math.trunc((n - GFG.maxn) / float(4)) + 1
            return t + dp [n - 4 * t]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12
        dp = GFG.precompute()
        print(GFG.Maximum_Summands(dp, n))
