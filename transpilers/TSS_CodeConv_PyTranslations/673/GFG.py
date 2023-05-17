class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def lcs(X, Y, m, n):
        L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 or j == 0:
                    L [i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L [i][j] = L [i - 1][j - 1] + 1
                else:
                    L [i][j] = max(L [i - 1][j], L [i][j - 1])
        return L [m][n]
    @staticmethod
    def findMinCost(X, Y, costX, costY):
        m = len(X)
        n = len(Y)
        len_LCS = 0
        len_LCS = GFG.lcs(X, Y, m, n)
        return costX * (m - len_LCS) + costY * (n - len_LCS)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        X = "ef"
        Y = "gh"
        print("Minimum Cost to make two strings " + " identical is = " + str(GFG.findMinCost(X, Y, 10, 20)))
