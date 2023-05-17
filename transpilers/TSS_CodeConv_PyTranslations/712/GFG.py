import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def print(n):
        print(n + math.trunc(n / float(2)))
        for i in range(2, n + 1, 2):
            print(str(i) + " ", end = '')
        for i in range(1, n + 1, 2):
            print(str(i) + " ", end = '')
        for i in range(2, n + 1, 2):
            print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        GFG.print(n)
