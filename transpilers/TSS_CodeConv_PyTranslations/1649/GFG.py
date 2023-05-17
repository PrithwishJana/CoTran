import math

class GFG:
    @staticmethod
    def snoob(x):
        rightOne = 0
        nextHigherOneBit = 0
        rightOnesPattern = 0
        next = 0
        if x > 0:
            rightOne = x & - x
            nextHigherOneBit = x + rightOne
            rightOnesPattern = x ^ nextHigherOneBit
            rightOnesPattern = math.trunc((rightOnesPattern) / float(rightOne))
            rightOnesPattern >>= 2
            next = nextHigherOneBit | rightOnesPattern
        return next
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 156
        print("Next higher number with same" + "number of set bits is " + str(GFG.snoob(x)))
