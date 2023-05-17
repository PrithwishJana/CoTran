import math

class GFG:
    @staticmethod
    def printPossible(a, b, c):
        if math.fmod((a + b + c), 2) != 0 or a + b < c:
            print("NO")
        else:
            print("YES")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 4
        c = 2
        GFG.printPossible(a, b, c)
