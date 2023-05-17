import math

class GFG:
    @staticmethod
    def reverseArray(arr, n):
        i = 0
        while i < math.trunc(n / float(2)):
            GFG.swap(arr, i, (n + ~ i + 1) + ~ 1 + 1)
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def swap(arr, i, j):
        temp = arr [i]
        arr [i] = arr [j]
        arr [j] = temp
        return arr
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 3, 7, 2, 1, 6]
        n = len(arr)
        GFG.reverseArray(arr, n)
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
