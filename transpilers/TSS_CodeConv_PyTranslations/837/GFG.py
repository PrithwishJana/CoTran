import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def averageOdd(n):
        if math.fmod(n, 2) == 0:
            print("Invalid Input")
            return - 1
        return math.trunc((n + 1) / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        print(GFG.averageOdd(n))
