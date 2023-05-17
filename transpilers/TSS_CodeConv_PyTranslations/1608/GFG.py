import math

class GFG:
    @staticmethod
    def productDiagonals(arr, n):
        product = 1
        for i in range(0, n):
            product = product * arr [i][i]
            product = product * arr [i][n - i - 1]
        if math.fmod(n, 2) == 1:
            product = math.trunc(product / float(arr [math.trunc(n / float(2))][math.trunc(n / float(2))]))
        return product
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr1 = [[ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 7, 4, 2 ], [ 2, 2, 2, 1 ]]
        print(str(GFG.productDiagonals(arr1, 4)) + "\n", end = '')
        arr2 = [[ 2, 1, 2, 1, 2 ], [ 1, 2, 1, 2, 1 ], [ 2, 1, 2, 1, 2 ], [ 1, 2, 1, 2, 1 ], [ 2, 1, 2, 1, 2 ]]
        print(str(GFG.productDiagonals(arr2, 5)) + "\n", end = '')
