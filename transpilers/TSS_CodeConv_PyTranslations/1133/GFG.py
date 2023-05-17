class GFG:
    @staticmethod
    def FindMinimumCost(ind, a, n, k, dp):
        if ind == (n - 1):
            return 0
        elif dp [ind] != - 1:
            return dp [ind]
        else:
            ans = Integer.MAX_VALUE
            for i in range(1, k + 1):
                if ind + i < n:
                    ans = min(ans, abs(a [ind + i] - a [ind]) + GFG.FindMinimumCost(ind + i, a, n, k, dp))
                else:
                    break
            return dp [ind] = ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [10, 30, 40, 50, 20]
        k = 3
        n = len(a)
        dp = [0 for _ in range(n)]
        Arrays.fill(dp, - 1)
        print(GFG.FindMinimumCost(0, a, n, k, dp))
