import math

class GFG:
    @staticmethod
    def areaOfKite(d1, d2):
        area = math.trunc((d1 * d2) / float(2))
        return area
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        d1 = 4
        d2 = 6
        print("Area of Kite = " + str(GFG.areaOfKite(d1, d2)))
