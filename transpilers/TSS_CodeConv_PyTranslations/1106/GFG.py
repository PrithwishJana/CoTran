import math

class GFG:
    PI = 3.14
    @staticmethod
    def find_area(r, d):
        R = d / GFG.PI
        R += r ** 2
        R = math.sqrt(R)
        area = GFG.PI * R ** 2
        return area
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        r = 4
        d = 5
        print(GFG.find_area(r, d))
