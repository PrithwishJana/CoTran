import math

class A1613:
    _POWER = [1, 10, 100, 1000, 10000, 100000]
    @staticmethod
    def main(args):
        s = java.util.Scanner(System.in)
        noOfComparison = s.nextInt()
        for i in range(0, noOfComparison):
            x1 = s.nextInt()
            p1 = s.nextInt()
            x2 = s.nextInt()
            p2 = s.nextInt()
            A1613._compare(x1, p1, x2, p2)
    @staticmethod
    def _compare(x1, p1, x2, p2):
        if p1 == p2:
            A1613._directCompare(x1, x2)
        else:
            xx1 = x1
            xx2 = x2
            while math.fmod(xx1, 10) == 0:
                xx1 /= 10
                p1 += 1
            while math.fmod(xx2, 10) == 0:
                xx2 /= 10
                p2 += 1
            if p1 > p2:
                xx1 *= A1613._cachedPower(p1 - p2)
            elif p2 > p1:
                xx2 *= A1613._cachedPower(p2 - p1)
            A1613._directCompare(xx1, xx2)
    @staticmethod
    def _cachedPower(p):
        if p < 6:
            return A1613._POWER [p]
        else:
            return 10 ** (p)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _directCompare(x1, x2):
        if x1 > x2:
            print(">")
        elif x2 > x1:
            print("<")
        else:
            print("=")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _directCompare(x1, x2):
        if x1 > x2:
            print(">")
        elif x2 > x1:
            print("<")
        else:
            print("=")
