class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def totalWays(N, M, X):
        dp = [[0 for _ in range(2)] for _ in range(N + 1)]
        if X == 1:
            dp [0][0] = 1
        else:
            dp [0][1] = 0
        if X == 1:
            dp [1][0] = 0
            dp [1][1] = M - 1
        else:
            dp [1][0] = 1
            dp [1][1] = (M - 2)
        for i in range(2, N):
            dp [i][0] = dp [i - 1][1]
            dp [i][1] = dp [i - 1][0] * (M - 1) + dp [i - 1][1] * (M - 2)
        return dp [N - 1][0]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 4
        M = 3
        X = 2
        print(GFG.totalWays(N, M, X))
