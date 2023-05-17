class LongestCommonSubSequence:
    @staticmethod
    def LCSubStr(X, Y, m, n):
        LCStuff = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        result = 0
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 or j == 0:
                    LCStuff [i][j] = 0
                elif X [i - 1] == Y [j - 1]:
                    LCStuff [i][j] = LCStuff [i - 1][j - 1] + 1
                    result = Integer.max(result, LCStuff [i][j])
                else:
                    LCStuff [i][j] = 0
        return result
    @staticmethod
    def main(args):
        X = "OldSite:GeeksforGeeks.org"
        Y = "NewSite:GeeksQuiz.com"
        m = len(X)
        n = len(Y)
        print("Length of Longest Common Substring is " + str(LongestCommonSubSequence.LCSubStr(X.toCharArray(), Y.toCharArray(), m, n)))
