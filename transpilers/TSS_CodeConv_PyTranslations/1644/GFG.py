class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(X, Y, N, K):
        count = [0 for _ in range(N + 1)]
        sol = 0
        count [0] = 0
        for i in range(1, N + 1):
            count [i] = count [i - 1] + abs(X[i - 1] - Y[i - 1])
        j = 0
        for i in range(1, N + 1):
            while (count [i] - count [j]) > K:
                j += 1
            sol = max(sol, i - j)
        return sol
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 4
        X = "abcd"
        Y = "bcde"
        K = 3
        print(str(GFG.solve(X, Y, N, K)) + "\n", end = '')
