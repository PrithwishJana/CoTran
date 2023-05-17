class GFG:
    @staticmethod
    def numberOfPaths(m, n):
        count = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            count [i][0] = 1
        for j in range(0, n):
            count [0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                count [i][j] = count [i - 1][j] + count [i][j - 1]
        return count [m - 1][n - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.numberOfPaths(3, 3))
