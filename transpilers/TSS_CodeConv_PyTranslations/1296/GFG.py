import math

class GFG:
    @staticmethod
    def binarySearch(arr, low, high):
        if high < low:
            return - 1
        mid = math.trunc((low + high) / float(2))
        midValue = arr [mid]
        if mid == arr [mid]:
            return mid
        leftindex = min(mid - 1, midValue)
        left = GFG.binarySearch(arr, low, leftindex)
        if left >= 0:
            return left
        rightindex = max(mid + 1, midValue)
        right = GFG.binarySearch(arr, rightindex, high)
        return right
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [- 10, - 5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
        print("Fixed Point is " + str(GFG.binarySearch(arr, 0, len(arr) - 1)))
        arr1 = [- 10, - 1, 3, 3, 10, 30, 30, 50, 100]
        print("Fixed Point is " + str(GFG.binarySearch(arr1, 0, len(arr1) - 1)))
