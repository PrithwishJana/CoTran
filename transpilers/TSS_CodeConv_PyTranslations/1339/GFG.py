import math

class GFG:
    @staticmethod
    def isPossibleToMakeDivisible(arr, n):
        remainder = 0
        for i in range(0, n):
            remainder = math.fmod((remainder + arr [i]), 3)
        return (remainder == 0)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [40, 50, 90]
        n = 3
        if GFG.isPossibleToMakeDivisible(arr, n):
            print("Yes\n", end = '')
        else:
            print("No\n", end = '')
