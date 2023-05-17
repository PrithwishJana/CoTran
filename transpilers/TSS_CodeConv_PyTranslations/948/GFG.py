import math

class GFG:
    @staticmethod
    def getRemainder(num, divisor):
        return (num - divisor * (math.trunc(num / float(divisor))))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.getRemainder(100, 7))
