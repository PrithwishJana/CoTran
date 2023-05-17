import math

class GFG:
    @staticmethod
    def countNonIncreasing(arr, n):
        cnt = 0
        len = 1
        i = 0
        while i < n - 1:
            if arr [i + 1] >= arr [i]:
                len += 1
            else:
                cnt += (math.trunc(((len + 1) * len) / float(2)))
                len = 1
            i += 1
        if len > 1:
            cnt += (math.trunc(((len - 1) * len) / float(2)))
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 2, 3, 7, 1, 1]
        n = len(arr)
        print(GFG.countNonIncreasing(arr, n))
