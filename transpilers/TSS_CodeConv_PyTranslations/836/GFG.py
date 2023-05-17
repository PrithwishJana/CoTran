import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def averageOdd(n):
        if math.fmod(n, 2) == 0:
            print("Invalid Input")
            return - 1
        sum = 0
        count = 0
        while n >= 1:
            count += 1
            sum += n
            n = n - 2
        return math.trunc(sum / float(count))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        print(GFG.averageOdd(n))
