import math

class GFG:
    @staticmethod
    def maximum_middle_value(n, k, arr):
        ans = - 1
        low = math.trunc((n + 1 - k) / float(2))
        high = math.trunc((n + 1 - k) / float(2)) + k
        for i in range(low, high + 1):
            ans = max(ans, arr [i - 1])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        k = 2
        arr = [9, 5, 3, 7, 10]
        print(GFG.maximum_middle_value(n, k, arr))
        n = 9
        k = 3
        arr1 = [2, 4, 3, 9, 5, 8, 7, 6, 10]
        print(GFG.maximum_middle_value(n, k, arr1))
