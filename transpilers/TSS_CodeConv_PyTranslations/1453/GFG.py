import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(arr, n):
        even = 0
        odd = 0
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 0:
                even += 1
            else:
                odd += 1
        print((even) * (n - 1))
        print((odd) * (n - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 5]
        n = len(arr)
        GFG.countPairs(arr, n)
