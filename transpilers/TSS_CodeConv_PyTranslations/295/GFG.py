import math

class GFG:
    @staticmethod
    def setBitNumber(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        k = int((math.log(n) / math.log(2)))
        return int((2 ** k))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        n = 273
        print(GFG.setBitNumber(n))
