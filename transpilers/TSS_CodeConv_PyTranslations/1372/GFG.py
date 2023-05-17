import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSteps(x, y):
        if math.fmod(x, y) == 0:
            return math.trunc(x / float(y))
        return math.trunc(x / float(y)) + GFG.countSteps(y, math.fmod(x, y))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 100
        y = 19
        print(GFG.countSteps(x, y))
