import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(n, a, b):
        sum = 0
        for i in range(0, n):
            if math.fmod(i, a) == 0 or math.fmod(i, b) == 0:
                sum += i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        a = 3
        b = 5
        print(GFG.findSum(n, a, b))
