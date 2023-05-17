class GFG:
    N = 5
    @staticmethod
    def printSumTricky(mat, k):
        if k > GFG.N:
            return
        stripSum = [[0 for _ in range(GFG.N)] for _ in range(GFG.N)]
        j = 0
        while j < GFG.N:
            sum = 0
            for i in range(0, k):
                sum += mat [i][j]
            stripSum [0][j] = sum
            i = 1
            while i < GFG.N - k + 1:
                sum += (mat [i + k - 1][j] - mat [i - 1][j])
                stripSum [i][j] = sum
                i += 1
            j += 1
        i = 0
        while i < GFG.N - k + 1:
            sum = 0
            for j in range(0, k):
                sum += stripSum [i][j]
            print(str(sum) + " ", end = '')
            j = 1
            while j < GFG.N - k + 1:
                sum += (stripSum [i][j + k - 1] - stripSum [i][j - 1])
                print(str(sum) + " ", end = '')
                j += 1
            print()
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        mat = [[ 1, 1, 1, 1, 1 ], [ 2, 2, 2, 2, 2 ], [ 3, 3, 3, 3, 3 ], [ 4, 4, 4, 4, 4 ], [ 5, 5, 5, 5, 5 ]]
        k = 3
        GFG.printSumTricky(mat, k)
