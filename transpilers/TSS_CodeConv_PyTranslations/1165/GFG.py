import math

class GFG:
    @staticmethod
    def centeredOctahedral(n):
        return math.trunc((2 * n + 1) * (2 * n * n + 2 * n + 3) / float(3))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.centeredOctahedral(n), end = '')
        print()
        n = 9
        print(GFG.centeredOctahedral(n), end = '')
