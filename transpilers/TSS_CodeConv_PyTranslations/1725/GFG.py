class GFG:
    @staticmethod
    def minStepToDeleteString(str):
        N = len(str)
        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(0, N + 1):
            for j in range(0, N + 1):
                dp [i][j] = 0
        for len in range(1, N + 1):
            i = 0
            j = len - 1
            while j < N:
                if len == 1:
                    dp [i][j] = 1
                else:
                    dp [i][j] = 1 + dp [i + 1][j]
                    if str[i] == str[i + 1]:
                        dp [i][j] = min(1 + dp [i + 2][j], dp [i][j])
                    for K in range(i + 2, j + 1):
                        if str[i] == str[K]:
                            dp [i][j] = min(dp [i + 1][K - 1] + dp [K + 1][j], dp [i][j])
                i += 1
                j += 1
        return dp [0][N - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "2553432"
        print(GFG.minStepToDeleteString(str))
