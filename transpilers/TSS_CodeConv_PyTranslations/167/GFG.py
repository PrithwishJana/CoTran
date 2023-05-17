import math

class GFG:
    @staticmethod
    def smallestIndexsum(arr, n):
        i = n - 1
        while i >= 0 and math.fmod(arr [i], 2) == 1:
            i -= 1
        sum = 0
        for j in range(0, i + 1):
            sum += arr [j]
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 5, 6, 3, 3]
        n = len(arr)
        print(GFG.smallestIndexsum(arr, n))
