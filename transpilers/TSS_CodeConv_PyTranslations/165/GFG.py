class GFG:
    N = 5
    @staticmethod
    def FindMaxProduct(arr, n):
        max = 0
        result = 0
        for i in range(0, n):
            for j in range(0, n):
                if (j - 3) >= 0:
                    result = arr [i][j] * arr [i][j - 1] * arr [i][j - 2] * arr [i][j - 3]
                    if max < result:
                        max = result
                if (i - 3) >= 0:
                    result = arr [i][j] * arr [i - 1][j] * arr [i - 2][j] * arr [i - 3][j]
                    if max < result:
                        max = result
                if (i - 3) >= 0 and (j - 3) >= 0:
                    result = arr [i][j] * arr [i - 1][j - 1] * arr [i - 2][j - 2] * arr [i - 3][j - 3]
                    if max < result:
                        max = result
                if (i - 3) >= 0 and (j - 1) <= 0:
                    result = arr [i][j] * arr [i - 1][j + 1] * arr [i - 2][j + 2] * arr [i - 3][j + 3]
                    if max < result:
                        max = result
        return max
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [[ 1, 2, 3, 4, 5 ], [ 6, 7, 8, 9, 1 ], [ 2, 3, 4, 5, 6 ], [ 7, 8, 9, 1, 0 ], [ 9, 6, 4, 2, 3 ]]
        print(GFG.FindMaxProduct(arr, GFG.N))
