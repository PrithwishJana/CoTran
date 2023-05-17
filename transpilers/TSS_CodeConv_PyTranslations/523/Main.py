import math

class solution:
    @staticmethod
    def count(arr, n, x):
        if x == 1:
            ans = int(2) ** n - 1
            return ans
        count = 0
        for i in range(0, n):
            if math.fmod(arr [i], x) == 0:
                count += 1
        ans = int(2) ** count - 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 4, 3, 5]
        n = len(arr)
        x = 1
        print(solution.count(arr, n, x))
