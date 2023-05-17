import math

class GFG:
    @staticmethod
    def findDigits(n, b):
        if n < 0:
            return 0
        if n <= 1:
            return 1
        M_PI = 3.141592
        M_E = 2.7182
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        x = ((n * math.log10(n / M_E) + math.log10(2 * M_PI * n) / 2.0)) / (math.log10(b))
        return int((math.floor(x) + 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(str(GFG.findDigits(4, 16)) + "\n", end = '')
        print(str(GFG.findDigits(5, 8)) + "\n", end = '')
        print(str(GFG.findDigits(12, 16)) + "\n", end = '')
        print(str(GFG.findDigits(19, 13)) + "\n", end = '')
