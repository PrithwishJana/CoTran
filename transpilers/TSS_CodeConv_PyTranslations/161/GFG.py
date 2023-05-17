import math

class GFG:
    @staticmethod
    def CntDivbyX(arr, n, x):
        number = 0
        count = 0
        for i in range(0, n):
            number = number * 2 + arr [i]
            if (math.fmod(number, x) == 0):
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 0, 1, 0, 1, 1, 0]
        n = len(arr)
        x = 2
        print(GFG.CntDivbyX(arr, n, x))
