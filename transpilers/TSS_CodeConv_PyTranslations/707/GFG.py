import math

class GFG:
    @staticmethod
    def checkPowerof8(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        i = math.log(n) / math.log(8)
        return (i - math.floor(i) < 0.000001)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 65
        if GFG.checkPowerof8(n):
            print("Yes")
        else:
            print("No")
