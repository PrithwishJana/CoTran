import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isHeap(arr, n):
        i = 0
        while i <= math.trunc((n - 2) / float(2)):
            if arr [2 * i + 1] > arr [i]:
                return False
            if 2 * i + 2 < n and arr [2 * i + 2] > arr [i]:
                return False
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [90, 15, 10, 7, 12, 2, 7, 3]
        n = len(arr)
        if GFG.isHeap(arr, n):
            print("Yes")
        else:
            print("No")
