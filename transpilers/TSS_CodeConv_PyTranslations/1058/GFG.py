import math

class GFG:
    @staticmethod
    def cube(h, r):
        if h < 0 and r < 0:
            return - 1
        a = (h * r * float(math.sqrt(2))) / (h + float(math.sqrt(2)) * r)
        return a
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        h = 5
        r = 6
        print(GFG.cube(h, r))
