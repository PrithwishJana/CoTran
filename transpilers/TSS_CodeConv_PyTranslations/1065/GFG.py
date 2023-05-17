import math

class GFG:
    @staticmethod
    def findPosition(k, n):
        f1 = 0
        f2 = 1
        f3 = 0
        i = 2
        while i != 0:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            if math.fmod(f2, k) == 0:
                return n * i
            i += 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        k = 4
        print("Position of n'th multiple" + " of k in Fibonacci Series is ", end = '')
        print(GFG.findPosition(k, n))
