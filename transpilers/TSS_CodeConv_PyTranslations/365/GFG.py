class GFG:
    @staticmethod
    def getMinimumOps(ar):
        n = len(ar)
        small = Collections.min(ar)
        large = Collections.max(ar)
        dp = [[0 for _ in range(large + 1)] for _ in range(n)]
        for j in range(small, large + 1):
            dp [0][j] = abs(ar[0] - j)
        for i in range(1, n):
            minimum = Integer.MAX_VALUE
            for j in range(small, large + 1):
                minimum = min(minimum, dp [i - 1][j])
                dp [i][j] = minimum + abs(ar[i] - j)
        ans = Integer.MAX_VALUE
        for j in range(small, large + 1):
            ans = min(ans, dp [n - 1][j])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 1, 4, 3]
        ar = list(Arrays.asList(arr))
        print(GFG.getMinimumOps(ar))
