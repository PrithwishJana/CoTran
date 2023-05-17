import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countCubes(a, b):
        return int((math.floor(Math.cbrt(b)) - math.ceil(Math.cbrt(a)) + 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 7
        b = 28
        print("Count of cubes is " + str(GFG.countCubes(a, b)), end = '')
