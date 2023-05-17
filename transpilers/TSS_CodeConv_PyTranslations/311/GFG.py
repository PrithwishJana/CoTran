import math

class GFG:
    @staticmethod
    def countSquares(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return (math.trunc(n * (n + 1) / float(2))) * (2 * n + 1) / 3
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print("Count of squares is " + str(GFG.countSquares(n)))
