import math

class GFG:
    @staticmethod
    def countNonDecreasing(n):
        N = 10
        count = 1
        for i in range(1, n + 1):
            count *= (N + i - 1)
            count = math.trunc(count / float(i))
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.countNonDecreasing(n), end = '')
