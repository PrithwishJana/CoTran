import math

class GFG:
    @staticmethod
    def area_of_regular_polygon(n, len):
        P = (len * n)
        A = len / (2 * math.tan((180 / n) * 3.14159 / 180))
        area = (P * A) / 2
        return area
    @staticmethod
    def area_of_triangle_inscribed(n, len):
        area = GFG.area_of_regular_polygon(n, len)
        triangle = area / n
        ins_tri = (triangle * 3)
        return ins_tri
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        n = 6
        len = 10
        print("{0:.3f}".format(GFG.area_of_triangle_inscribed(n, len)), end = '')
