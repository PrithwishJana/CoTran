class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def lps(str):
        n = len(str)
        L = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(0, n):
            L [i][i] = 1
        for cl in range(2, n + 1):
            i = 0
            while i < n - cl + 1:
                j = i + cl - 1
                if str[i] == str[j] and cl == 2:
                    L [i][j] = 2
                elif str[i] == str[j]:
                    L [i][j] = L [i + 1][j - 1] + 2
                else:
                    L [i][j] = Integer.max(L [i][j - 1], L [i + 1][j])
                i += 1
        return L [0][n - 1]
    @staticmethod
    def minimumNumberOfDeletions(str):
        n = len(str)
        len = GFG.lps(str)
        return (n - len)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        print("Minimum number " + "of deletions = " + str(GFG.minimumNumberOfDeletions(str)))
