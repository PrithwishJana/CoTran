import math

class GFG:
    @staticmethod
    def countMultiples(n):
        return math.trunc(n / float(3)) + math.trunc(n / float(7)) - math.trunc(n / float(21))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("Count = " + str(GFG.countMultiples(25)))
