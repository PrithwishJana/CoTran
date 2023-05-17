import math

class GFG:
    @staticmethod
    def firstDigit(n):
        digits = int((math.log10(n)))
        n = int((math.trunc(n / float(int((10 ** digits))))))
        return n
    @staticmethod
    def lastDigit(n):
        return (math.fmod(n, 10))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 98562
        print(str(GFG.firstDigit(n)) + " " + str(GFG.lastDigit(n)))
