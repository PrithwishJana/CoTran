class GFG:
    MAX = 10
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def lcs(dp, arr1, n, arr2, m, k):
        if k < 0:
            return - 10000000
        if n < 0 or m < 0:
            return 0
        ans = dp [n][m][k]
        if ans != - 1:
            return ans
        try:
            ans = max(GFG.lcs(dp, arr1, n - 1, arr2, m, k), GFG.lcs(dp, arr1, n, arr2, m - 1, k))
            if arr1 [n - 1] == arr2 [m - 1]:
                ans = max(ans, 1 + GFG.lcs(dp, arr1, n - 1, arr2, m - 1, k))
            ans = max(ans, 1 + GFG.lcs(dp, arr1, n - 1, arr2, m - 1, k - 1))
        except Exception as e:
            pass
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 1
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [5, 3, 1, 4, 2]
        n = len(arr1)
        m = len(arr2)
        dp = [[[0 for _ in range(GFG.MAX)] for _ in range(GFG.MAX)] for _ in range(GFG.MAX)]
        i = 0
        while i < GFG.MAX:
            j = 0
            while j < GFG.MAX:
                l = 0
                while l < GFG.MAX:
                    dp [i][j][l] = - 1
                    l += 1
                j += 1
            i += 1
        print(GFG.lcs(dp, arr1, n, arr2, m, k))
