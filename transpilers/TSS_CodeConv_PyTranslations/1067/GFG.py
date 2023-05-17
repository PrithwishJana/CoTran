class GFG:
    @staticmethod
    def countMinimumMoves(arr, n, k):
        i = 0
        for i in range(k - 1, n):
            if arr [i] != arr [k - 1]:
                return - 1
        for i in range(k - 1, -1, -1):
            if arr [i] != arr [k - 1]:
                return i + 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4]
        K = 4
        n = len(arr)
        print(GFG.countMinimumMoves(arr, n, K), end = '')
