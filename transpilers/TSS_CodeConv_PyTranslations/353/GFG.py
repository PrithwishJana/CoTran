class GFG:
    MAX = 1000
    @staticmethod
    def maxSubsequenceSubstring(x, y, n, m):
        dp = [[0 for _ in range(GFG.MAX)] for _ in range(GFG.MAX)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                dp [i][j] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x [j - 1] == y [i - 1]:
                    dp [i][j] = 1 + dp [i - 1][j - 1]
                else:
                    dp [i][j] = dp [i][j - 1]
        ans = 0
        for i in range(1, m + 1):
            ans = max(ans, dp [i][n])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = "ABCD" .toCharArray()
        y = "BACDBDCD" .toCharArray()
        n = len(x)
        m = len(y)
        print(GFG.maxSubsequenceSubstring(x, y, n, m))
