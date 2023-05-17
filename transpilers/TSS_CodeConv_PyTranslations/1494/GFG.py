import math

class GFG:
    @staticmethod
    def printDuplicates(arr, n):
        i = 0
        fl = 0
        for i in range(0, n):
            if arr [math.fmod(arr [i], n)] >= n:
                if arr [math.fmod(arr [i], n)] < 2 * n:
                    print(math.fmod(arr [i], n) + " ", end = '')
                    fl = 1
            arr [math.fmod(arr [i], n)] += n
        if not(fl > 0):
            print("-1")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 6, 3, 1, 3, 6, 6]
        arr_size = len(arr)
        GFG.printDuplicates(arr, arr_size)
