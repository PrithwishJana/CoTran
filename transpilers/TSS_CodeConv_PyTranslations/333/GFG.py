import math

class GFG:
    @staticmethod
    def nextPowerOf2(n):
        count = 0
        if n != 0 and (n & (n - 1)) == 0:
            return n
        while n != 0:
            n >>= 1
            count += 1
        return 1 << count
    @staticmethod
    def removeElement(n):
        if n == 1 or n == 2:
            return 0
        a = GFG.nextPowerOf2(n)
        if n == a or n == a - 1:
            return 1
        elif n == a - 2:
            return 0
        elif math.fmod(n, 2) == 0:
            return 1
        else:
            return 2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print(GFG.removeElement(n))
