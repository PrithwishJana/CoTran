import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minCost(arr, n):
        count_even = 0
        count_odd = 0
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 0:
                count_even += 1
            else:
                count_odd += 1
        return min(count_even, count_odd)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 4, 3, 1, 5]
        n = len(arr)
        print(GFG.minCost(arr, n))
