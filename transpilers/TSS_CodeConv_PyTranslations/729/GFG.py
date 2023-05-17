import math

class GFG:
    @staticmethod
    def calculate_min_sum(a, n):
        a.sort()
        min_sum = 0
        for i in range(1, n, 2):
            min_sum += abs(a [i] - a [i - 1])
        return min_sum
    @staticmethod
    def calculate_max_sum(a, n):
        a.sort()
        max_sum = 0
        i = 0
        while i < math.trunc(n / float(2)):
            max_sum += abs(a [n - 1 - i] - a [i])
            i += 1
        return max_sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [10, - 10, 20, - 40]
        n = len(a)
        print("The minimum sum of pairs is " + str(GFG.calculate_min_sum(a, n)))
        print("The maximum sum of pairs is " + str(GFG.calculate_max_sum(a, n)))
