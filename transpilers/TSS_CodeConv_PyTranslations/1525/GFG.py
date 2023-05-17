import math

class GFG:
    @staticmethod
    def replaceDigit(x, d1, d2):
        result = 0
        multiply = 1
        while math.fmod(x, 10) > 0:
            remainder = math.fmod(x, 10)
            if remainder == d1:
                result = result + d2 * multiply
            else:
                result = result + remainder * multiply
            multiply *= 10
            x = math.trunc(x / float(10))
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 645
        d1 = 6
        d2 = 5
        print(GFG.replaceDigit(x, d1, d2))
