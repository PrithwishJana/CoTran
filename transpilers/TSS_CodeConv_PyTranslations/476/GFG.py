import math

class GFG:
    @staticmethod
    def find_Area(a):
        R = a * float((2.0 - math.sqrt(2)))
        area = float(((3.14 * R * R) / 2.0))
        return area
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 4
        print(" Area of semicircle = " + "{0:.4f}".format(GFG.find_Area(a)))
