import math

class GFG:
    @staticmethod
    def sum_even_and_even_index(arr, n):
        i = 0
        sum = 0
        for i in range(0, n, 2):
            if math.fmod(arr [i], 2) == 0:
                sum += arr [i]
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 6, 12, 1, 18, 8]
        n = len(arr)
        print("Sum of even numbers" + " at even indices is " + + GFG.sum_even_and_even_index(arr, n))
