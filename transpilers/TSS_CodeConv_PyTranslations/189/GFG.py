import math

class GFG:
    @staticmethod
    def maximumAbsolute(arr, n):
        mn = Integer.MAX_VALUE
        mx = Integer.MIN_VALUE
        for i in range(0, n):
            if i > 0 and arr [i] == - 1 and arr [i - 1] != - 1:
                mn = min(mn, arr [i - 1])
                mx = max(mx, arr [i - 1])
            if i < n - 1 and arr [i] == - 1 and arr [i + 1] != - 1:
                mn = min(mn, arr [i + 1])
                mx = max(mx, arr [i + 1])
        common_integer = math.trunc((mn + mx) / float(2))
        for i in range(0, n):
            if arr [i] == - 1:
                arr [i] = common_integer
        max_diff = 0
        i = 0
        while i < n - 1:
            diff = abs(arr [i] - arr [i + 1])
            if diff > max_diff:
                max_diff = diff
            i += 1
        return max_diff
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [- 1, - 1, 11, - 1, 3, - 1]
        n = len(arr)
        print(GFG.maximumAbsolute(arr, n))
