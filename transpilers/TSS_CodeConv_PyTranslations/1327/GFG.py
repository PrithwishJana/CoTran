import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printNumbers(N):
        flag = 1
        x = N
        if N > 0:
            while x > 0 and flag == 1:
                digit = math.fmod(x, 10)
                if digit != 1 and digit != 3:
                    flag = 0
                x = math.trunc(x / float(10))
            if flag == 1:
                print(str(N) + " ", end = '')
            GFG.printNumbers(N - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 20
        GFG.printNumbers(N)
