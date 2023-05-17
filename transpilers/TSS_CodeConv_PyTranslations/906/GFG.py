import math

class GFG:
    @staticmethod
    def onesComplement(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        number_of_bits = int((math.floor(math.log(n) / math.log(2)))) + 1
        return ((1 << number_of_bits) - 1) ^ n
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 22
        print(GFG.onesComplement(n), end = '')
