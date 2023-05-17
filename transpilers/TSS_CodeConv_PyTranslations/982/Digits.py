import math

class Digits:
    @staticmethod
    def firstkdigits(n, k):
        product = 1
        for i in range(0, n):
            product *= n
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        while int((product / 10 ** k)) != 0:
            product = math.trunc(product / float(10))
        return product
    @staticmethod
    def main(args):
        n = 15
        k = 4
        print(Digits.firstkdigits(n, k))
