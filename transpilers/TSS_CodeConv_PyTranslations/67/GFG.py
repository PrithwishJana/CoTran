class GFG:
    @staticmethod
    def printKMax(arr, n, k):
        j = 0
        max = 0
        i = 0
        while i <= n - k:
            max = arr [i]
            for j in range(1, k):
                if arr [i + j] > max:
                    max = arr [i + j]
            print(str(max) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 3
        GFG.printKMax(arr, len(arr), k)
