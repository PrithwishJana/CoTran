class GFG:
    MAX = 100
    @staticmethod
    def countMountains(a, n):
        A = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        count = 0
        i = 0
        while i < n + 2:
            j = 0
            while j < n + 2:
                if (i == 0) or (j == 0) or (i == n + 1) or (j == n + 1):
                    A [i][j] = Integer.MIN_VALUE
                else:
                    A [i][j] = a [i - 1][j - 1]
                j += 1
            i += 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if (A [i][j] > A [i - 1][j]) and (A [i][j] > A [i + 1][j]) and (A [i][j] > A [i][j - 1]) and (A [i][j] > A [i][j + 1]) and (A [i][j] > A [i - 1][j - 1]) and (A [i][j] > A [i + 1][j + 1]) and (A [i][j] > A [i - 1][j + 1]) and (A [i][j] > A [i + 1][j - 1]):
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
        n = 3
        print(GFG.countMountains(a, n), end = '')
