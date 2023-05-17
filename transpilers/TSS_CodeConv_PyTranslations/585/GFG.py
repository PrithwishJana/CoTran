import math

class GFG:
    @staticmethod
    def findAngle(n):
        interiorAngle = 0
        exteriorAngle = 0
        interiorAngle = math.trunc((n - 2) * 180 / float(n))
        exteriorAngle = math.trunc(360 / float(n))
        print("Interior angle: " + str(interiorAngle))
        print("Exterior angle: " + str(exteriorAngle))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        GFG.findAngle(n)
