import math

class GFG:
    @staticmethod
    def isPowerOfTwo(n):
        if n == 0:
            return False
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return int((math.ceil((math.log(n) / math.log(2))))) == int((math.floor(((math.log(n) / math.log(2))))))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        if GFG.isPowerOfTwo(31):
            print("Yes")
        else:
            print("No")
        if GFG.isPowerOfTwo(64):
            print("Yes")
        else:
            print("No")
