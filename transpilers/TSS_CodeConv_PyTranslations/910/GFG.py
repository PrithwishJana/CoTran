import math

class GFG:
    @staticmethod
    def alter(x, y):
        while True:
            if x == 0 or y == 0:
                break
            if x >= 2 * y:
                x = math.fmod(x, (2 * y))
            elif y >= 2 * x:
                y = math.fmod(y, (2 * x))
            else:
                break
        print("X = " + str(x) + ", " + "Y = " + str(y))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 12
        y = 5
        GFG.alter(x, y)
