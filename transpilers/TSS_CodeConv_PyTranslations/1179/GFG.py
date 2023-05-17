import math

class GFG:
    @staticmethod
    def _next(arr, target):
        start = 0
        end = len(arr) - 1
        ans = - 1
        while start <= end:
            mid = math.trunc((start + end) / float(2))
            if arr [mid] <= target:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 5, 8, 12]
        print(GFG._next(arr, 8))
