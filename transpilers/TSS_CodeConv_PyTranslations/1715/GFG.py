import math

class GFG:
    @staticmethod
    def findHypotenuse(side1, side2):
        h = math.sqrt((side1 * side1) + (side2 * side2))
        return h
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(s):
        side1 = 3
        side2 = 4
        print("{0:.2f}".format(GFG.findHypotenuse(side1, side2)), end = '')
