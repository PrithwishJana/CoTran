import math

class BinarySearch:
    @staticmethod
    def countRotations(arr, low, high):
        if high < low:
            return 0
        if high == low:
            return low
        mid = low + math.trunc((high - low) / float(2))
        if mid < high and arr [mid + 1] < arr [mid]:
            return (mid + 1)
        if mid > low and arr [mid] < arr [mid - 1]:
            return mid
        if arr [high] > arr [mid]:
            return BinarySearch.countRotations(arr, low, mid - 1)
        return BinarySearch.countRotations(arr, mid + 1, high)
    @staticmethod
    def main(args):
        arr = [15, 18, 2, 3, 6, 12]
        n = len(arr)
        print(BinarySearch.countRotations(arr, 0, n - 1))
