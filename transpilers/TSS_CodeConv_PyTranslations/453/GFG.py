import math

class GFG:
    @staticmethod
    def sumDivisibles(A, B, M):
        sum = 0
        for i in range(A, B + 1):
            if math.fmod(i, M) == 0:
                sum += i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = 6
        B = 15
        M = 3
        print(str(GFG.sumDivisibles(A, B, M)) + "\n", end = '')
