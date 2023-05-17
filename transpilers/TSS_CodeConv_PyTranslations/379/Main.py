class solution:
    MAX = 4
    @staticmethod
    def countWays(index, cnt, dp, n, m, k):
        if index == n:
            if cnt == k:
                return 1
            else:
                return 0
        if dp [index][cnt] != - 1:
            return dp [index][cnt]
        ans = 0
        ans += solution.countWays(index + 1, cnt, dp, n, m, k)
        ans += (m - 1) * solution.countWays(index + 1, cnt + 1, dp, n, m, k)
        return dp [index][cnt] = ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        m = 3
        k = 2
        dp = [[0 for _ in range(solution.MAX)] for _ in range(n + 1)]
        i = 0
        while i < n + 1:
            for j in range(0, solution.MAX):
                dp [i][j] = - 1
            i += 1
        print(m * solution.countWays(1, 0, dp, n, m, k))
