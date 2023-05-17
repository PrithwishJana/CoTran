class LCS_3Strings:
    @staticmethod
    def lcsOf3(X, Y, Z, m, n, o):
        L = [[[0 for _ in range(o + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                for k in range(0, o + 1):
                    if i == 0 or j == 0 or k == 0:
                        L [i][j][k] = 0
                    elif X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                        L [i][j][k] = L [i - 1][j - 1][k - 1] + 1
                    else:
                        L [i][j][k] = max(max(L [i - 1][j][k], L [i][j - 1][k]), L [i][j][k - 1])
        return L [m][n][o]
    @staticmethod
    def main(args):
        X = "AGGT12"
        Y = "12TXAYB"
        Z = "12XBA"
        m = len(X)
        n = len(Y)
        o = len(Z)
        print("Length of LCS is " + str(LCS_3Strings.lcsOf3(X, Y, Z, m, n, o)))
