import math

class GFG:
    @staticmethod
    def numberOfMinutes(S, S1):
        Min = 0
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        Min = int((((S - S1) / math.floor(S)) * 60))
        return Min
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        S = 30
        S1 = 10
        print(str(GFG.numberOfMinutes(S, S1)) + " min")
