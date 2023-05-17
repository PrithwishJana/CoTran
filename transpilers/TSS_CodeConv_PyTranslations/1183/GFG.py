class GFG:
    @staticmethod
    def TotalWays(n, s, k):
        dp = [0 for _ in range(n)]
        dp [s - 1] = 1
        for i in range(s, n):
            idx = max(s - 1, i - k)
            for j in range(idx, i):
                dp [i] += dp [j]
        return dp [n - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        k = 2
        s = 2
        print("Total Ways = " + str(GFG.TotalWays(n, s, k)), end = '')
