import math

class GFG:
    @staticmethod
    def polyarea(n, a):
        if a < 0 and n < 0:
            return - 1
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        A = (a * a * n) / float((4 * math.tan((180 / n) * math.pi / 180)))
        return A
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 9
        n = 6
        print("{0:.3f}".format(GFG.polyarea(n, a)))
