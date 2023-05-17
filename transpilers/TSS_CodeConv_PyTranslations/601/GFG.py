import math

class GFG:
    @staticmethod
    def findArea(a):
        area = 0
        area = float((5 * math.sqrt(3) * a * a))
        return area
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findVolume(a):
        volume = 0
        volume = float(((float(5) / 12) * (3 + math.sqrt(5)) * a * a * a))
        return volume
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 5
        print("Area: " + "{0:.2f}".format(GFG.findArea(a)))
        print("Volume: " + "{0:.2f}".format(GFG.findVolume(a)))
