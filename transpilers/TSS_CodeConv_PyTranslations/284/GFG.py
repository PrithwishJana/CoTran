import math

class GFG:
    @staticmethod
    def number_cake(n):
        return math.trunc((n * n * n + 5 * n + 6) / float(6))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        print(GFG.number_cake(n))
        n = 8
        print(GFG.number_cake(n))
        n = 25
        print(GFG.number_cake(n))
