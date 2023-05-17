import math

class GFG:
    @staticmethod
    def minAbsDiff(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        left = int(2) ** (int((math.log(n) / math.log(2))))
        right = left * 2
        return min((n - left), (right - n))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        print(GFG.minAbsDiff(n))
