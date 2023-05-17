import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def reverse(n):
        rev = 0
        while n != 0:
            rev = (rev * 10) + (math.fmod(n, 10))
            n = math.trunc(n / float(10))
        return rev
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getSum(n):
        n = GFG.reverse(n)
        sumOdd = 0
        sumEven = 0
        c = 1
        while n != 0:
            if math.fmod(c, 2) == 0:
                sumEven += math.fmod(n, 10)
            else:
                sumOdd += math.fmod(n, 10)
            n = math.trunc(n / float(10))
            c += 1
        print("Sum odd = " + str(sumOdd))
        print("Sum even = " + str(sumEven))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 457892
        GFG.getSum(n)
