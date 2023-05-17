import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isHeap(arr, i, n):
        if i > math.trunc((n - 2) / float(2)):
            return True
        if arr [i] >= arr [2 * i + 1] and arr [i] >= arr [2 * i + 2] and GFG.isHeap(arr, 2 * i + 1, n) and GFG.isHeap(arr, 2 * i + 2, n):
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [90, 15, 10, 7, 12, 2, 7, 3]
        n = len(arr) - 1
        if GFG.isHeap(arr, 0, n):
            print("Yes")
        else:
            print("No")
