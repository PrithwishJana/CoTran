import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSetBits(n):
        bitCount = 0
        for i in range(1, n + 1):
            bitCount += GFG.countSetBitsUtil(i)
        return bitCount
    @staticmethod
    def countSetBitsUtil(x):
        if x <= 0:
            return 0
        return (0 if math.fmod(x, 2) == 0 else 1) + GFG.countSetBitsUtil(math.trunc(x / float(2)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print("Total set bit count is ", end = '')
        print(GFG.countSetBits(n))
