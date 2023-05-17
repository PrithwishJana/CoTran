import math

class GFG:
    @staticmethod
    def productEqual(n):
        if n < 10:
            return False
        prodOdd = 1
        prodEven = 1
        while n > 0:
            digit = math.fmod(n, 10)
            prodOdd *= digit
            n = math.trunc(n / float(10))
            if n == 0:
                break
            digit = math.fmod(n, 10)
            prodEven *= digit
            n = math.trunc(n / float(10))
        if prodEven == prodOdd:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4324
        if GFG.productEqual(n):
            print("Yes")
        else:
            print("No")
