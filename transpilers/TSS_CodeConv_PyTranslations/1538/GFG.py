import math

class GFG:
    @staticmethod
    def indexOfFirstOne(arr, low, high):
        mid = 0
        while low <= high:
            mid = math.trunc((low + high) / float(2))
            if arr [mid] == 1 and (mid == 0 or arr [mid - 1] == 0):
                break
            elif arr [mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return mid
    @staticmethod
    def posOfFirstOne(arr):
        l = 0
        h = 1
        while arr [h] == 0:
            l = h
            h = 2 * h
        return GFG.indexOfFirstOne(arr, l, h)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [0, 0, 1, 1, 1, 1]
        print("Index = " + str(GFG.posOfFirstOne(arr)))
