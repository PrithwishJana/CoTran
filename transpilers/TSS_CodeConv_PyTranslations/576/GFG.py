import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(arr, n, left, right):
        k = right - left
        d = arr [1] - arr [0]
        ans = arr [left - 1] * (k + 1)
        ans = ans + math.trunc((d * (k * (k + 1))) / float(2))
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 4, 6, 8, 10, 12, 14, 16]
        queries = 3
        q = [[ 2, 4 ], [ 2, 6 ], [ 5, 6 ]]
        n = len(arr)
        for i in range(0, queries):
            print(str(GFG.findSum(arr, n, q [i][0], q [i][1])) + "\n", end = '')
