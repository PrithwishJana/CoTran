class GFG:
    N = 3
    @staticmethod
    def rotateMatrix(mat):
        for i in range(GFG.N - 1, -1, -1):
            for j in range(GFG.N - 1, -1, -1):
                print(str(mat [i][j]) + " ", end = '')
            print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
        GFG.rotateMatrix(mat)
