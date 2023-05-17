import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minSum(arr, n, x):
        sum = 0
        largestDivisible = - 1
        minimum = arr [0]
        for i in range(0, n):
            sum += arr [i]
            if math.fmod(arr [i], x) == 0 and largestDivisible < arr [i]:
                largestDivisible = arr [i]
            if arr [i] < minimum:
                minimum = arr [i]
        if largestDivisible == - 1:
            return sum
        sumAfterOperation = sum - minimum - largestDivisible + (x * minimum) + (math.trunc(largestDivisible / float(x)))
        return min(sum, sumAfterOperation)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 5, 5, 5, 6]
        n = len(arr)
        x = 3
        print(GFG.minSum(arr, n, x))
