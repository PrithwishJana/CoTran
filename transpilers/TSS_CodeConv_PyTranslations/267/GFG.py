import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printArray(arr, n):
        for i in range(0, n):
            print(str(arr [i]) + " ", end = '')
    @staticmethod
    def removeMin(arr, n):
        i = 0
        minVal = arr [0]
        for i in range(1, n):
            minVal = min(minVal, arr [i])
        for i in range(0, n):
            arr [i] = arr [i] - minVal
    @staticmethod
    def removeFromMax(arr, n):
        i = 0
        maxVal = arr [0]
        for i in range(1, n):
            maxVal = max(maxVal, arr [i])
        for i in range(0, n):
            arr [i] = maxVal - arr [i]
    @staticmethod
    def modifyArray(arr, n, k):
        if math.fmod(k, 2) == 0:
            GFG.removeMin(arr, n)
        else:
            GFG.removeFromMax(arr, n)
        GFG.printArray(arr, n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 8, 12, 16]
        n = len(arr)
        k = 2
        GFG.modifyArray(arr, n, k)
