import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printRoots(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        theta = math.pi * 2 / n
        for k in range(0, n):
            real = math.cos(k * theta)
            img = math.sin(k * theta)
            print("{0:.3f}".format(real), end = '')
            if img >= 0:
                print(" + i ", end = '')
            else:
                print(" - i ", end = '')
            print("{0:.3f}".format(abs(img)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.printRoots(1)
        GFG.printRoots(2)
        GFG.printRoots(3)
