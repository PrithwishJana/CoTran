import math

class GFG:
    M = 1001
    MOD = 998244353
    dp = [[0 for _ in range(M)] for _ in range(M)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(idx, diff, N, M, K):
        if idx > N:
            if diff == K:
                return 1
            return 0
        if GFG.dp [idx][diff] != - 1:
            return GFG.dp [idx][diff]
        ans = GFG.solve(idx + 1, diff, N, M, K)
        ans += (M - 1) * GFG.solve(idx + 1, diff + 1, N, M, K)
        return GFG.dp [idx][diff] = math.fmod(ans, GFG.MOD)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        M = 3
        K = 0
        for i in range(0, M + 1):
            for j in range(0, M + 1):
                GFG.dp [i][j] = - 1
        print((M * GFG.solve(2, 0, N, M, K)))
