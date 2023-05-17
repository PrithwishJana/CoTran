class LPS:
    @staticmethod
    def max(x, y):
        return x if (x > y) else y
    @staticmethod
    def lps(seq):
        n = len(seq)
        i = 0
        j = 0
        cl = 0
        L = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            L [i][i] = 1
        for cl in range(2, n + 1):
            i = 0
            while i < n - cl + 1:
                j = i + cl - 1
                if seq[i] == seq[j] and cl == 2:
                    L [i][j] = 2
                elif seq[i] == seq[j]:
                    L [i][j] = L [i + 1][j - 1] + 2
                else:
                    L [i][j] = LPS.max(L [i][j - 1], L [i + 1][j])
                i += 1
        return L [0][n - 1]
    @staticmethod
    def main(args):
        seq = "GEEKSFORGEEKS"
        n = len(seq)
        print("The length of the LPS is " + str(LPS.lps(seq)))
