import math

class GFG:
    @staticmethod
    def countGreater(arr, n, k):
        l = 0
        r = n - 1
        leftGreater = n
        while l <= r:
            m = l + math.trunc((r - l) / float(2))
            if arr [m] > k:
                leftGreater = m
                r = m - 1
            else:
                l = m + 1
        return (n - leftGreater)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 3, 4, 7, 7, 7, 11, 13, 13]
        n = len(arr)
        k = 7
        print(GFG.countGreater(arr, n, k))
