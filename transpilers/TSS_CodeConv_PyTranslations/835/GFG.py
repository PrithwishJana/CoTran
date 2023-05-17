class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def diagonalsMinMax(mat):
        n = len(mat)
        if n == 0:
            return
        principalMin = mat [0][0]
        principalMax = mat [0][0]
        secondaryMin = mat [n - 1][0]
        secondaryMax = mat [n - 1][0]
        for i in range(0, n):
            if mat [i][i] < principalMin:
                principalMin = mat [i][i]
            if mat [i][i] > principalMax:
                principalMax = mat [i][i]
            if mat [n - 1 - i][i] < secondaryMin:
                secondaryMin = mat [n - 1 - i][i]
            if mat [n - 1 - i][i] > secondaryMax:
                secondaryMax = mat [n - 1 - i][i]
        print("Principal Diagonal Smallest Element:  " + str(principalMin))
        print("Principal Diagonal Greatest Element : " + str(principalMax))
        print("Secondary Diagonal Smallest Element: " + str(secondaryMin))
        print("Secondary Diagonal Greatest Element: " + str(secondaryMax))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        matrix = [[ 1, 2, 3, 4, - 10 ], [ 5, 6, 7, 8, 6 ], [ 1, 2, 11, 3, 4 ], [ 5, 6, 70, 5, 8 ], [ 4, 9, 7, 1, - 5 ]]
        GFG.diagonalsMinMax(matrix)
