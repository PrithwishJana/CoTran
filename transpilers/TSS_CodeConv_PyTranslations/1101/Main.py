import math

class solution:
    @staticmethod
    def getSum(n, d):
        sum = 0
        for i in range(1, n + 1):
            if math.fmod(i, 10) == d:
                sum += i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 30
        d = 3
        print(solution.getSum(n, d))
