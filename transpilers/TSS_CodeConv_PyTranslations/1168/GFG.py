import math

class GFG:
    @staticmethod
    def leftRotate(arr, n, k):
        i = k
        while i < k + n:
            print(str(arr [math.fmod(i, n)]) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 3, 5, 7, 9]
        n = len(arr)
        k = 2
        GFG.leftRotate(arr, n, k)
        print()
        k = 3
        GFG.leftRotate(arr, n, k)
        print()
        k = 4
        GFG.leftRotate(arr, n, k)
        print()
