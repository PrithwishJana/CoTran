class GFG:
    N = 3
    @staticmethod
    def maxPathSum(tri, m, n):
        for i in range(m - 1, -1, -1):
            for j in range(0, i + 1):
                if tri [i + 1][j] > tri [i + 1][j + 1]:
                    tri [i][j] += tri [i + 1][j]
                else:
                    tri [i][j] += tri [i + 1][j + 1]
        return tri [0][0]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        tri = [[ 1, 0, 0 ], [ 4, 8, 0 ], [ 1, 5, 3 ]]
        print(GFG.maxPathSum(tri, 2, 2))
