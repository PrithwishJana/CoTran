import math

class GFG:
    @staticmethod
    def findMinIndex(arr, low, high):
        if high < low:
            return 0
        if high == low:
            return low
        mid = math.trunc((low + high) / float(2))
        if mid < high and arr [mid + 1] < arr [mid]:
            return (mid + 1)
        if mid > low and arr [mid] < arr [mid - 1]:
            return mid
        if arr [high] > arr [mid]:
            return GFG.findMinIndex(arr, low, mid - 1)
        return GFG.findMinIndex(arr, mid + 1, high)
    @staticmethod
    def binary_search(arr, l, h, x):
        while l <= h:
            mid = math.trunc((l + h) / float(2))
            if arr [mid] <= x:
                l = mid + 1
            else:
                h = mid - 1
        return h
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countEleLessThanOrEqual(arr, n, x):
        min_index = GFG.findMinIndex(arr, 0, n - 1)
        if x <= arr [n - 1]:
            return (GFG.binary_search(arr, min_index, n - 1, x) + 1 - min_index)
        if (min_index - 1) >= 0 and x <= arr [min_index - 1]:
            return (n - min_index + GFG.binary_search(arr, 0, min_index - 1, x) + 1)
        return n
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [6, 10, 12, 15, 2, 4, 5]
        n = len(arr)
        x = 14
        print("Count = " + str(GFG.countEleLessThanOrEqual(arr, n, x)), end = '')
