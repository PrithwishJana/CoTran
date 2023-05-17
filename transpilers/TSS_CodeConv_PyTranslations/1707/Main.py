class Solution:
    def isToeplitzMatrix(self, matrix):
        r = 1
        while r < len(matrix):
            c = 1
            while c < len(matrix [0]):
                if matrix [r - 1][c - 1] != matrix [r][c]:
                    return False
                c += 1
            r += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        matrix = [[ 1, 2, 3, 4 ], [ 5, 1, 2, 3 ], [ 9, 5, 1, 2 ]]
        out = sObj.isToeplitzMatrix(matrix)
        print(out)
