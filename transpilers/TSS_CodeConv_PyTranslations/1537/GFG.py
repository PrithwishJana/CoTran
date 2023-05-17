import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countDigits(a, b):
        if a == 0 or b == 0:
            return 1
        return int(math.floor(math.log10(abs(a)) + math.log10(abs(b)))) + 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 33
        b = - 24
        print(GFG.countDigits(a, b), end = '')
