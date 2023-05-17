import math

class GFG:
    @staticmethod
    def printLargestDivisible(n, a):
        i = 0
        c0 = 0
        c5 = 0
        for i in range(0, n):
            if a [i] == 0:
                c0 += 1
            else:
                c5 += 1
        c5 = int(math.floor(math.trunc(c5 / float(9)))) * 9
        if c0 == 0:
            print(- 1, end = '')
        elif c5 == 0:
            print(0)
        else:
            for i in range(0, c5):
                print(5, end = '')
            for i in range(0, c0):
                print(0, end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5]
        n = len(a)
        GFG.printLargestDivisible(n, a)
