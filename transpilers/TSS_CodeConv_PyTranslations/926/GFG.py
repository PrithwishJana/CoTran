import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fib(n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        phi = (1 + math.sqrt(5)) / 2
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        return int(round(phi ** n / math.sqrt(5)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculateSum(l, r):
        sum = GFG.fib(r + 2) - GFG.fib(l + 1)
        return sum
    @staticmethod
    def sumFibonacci(k):
        l = math.trunc((k * (k - 1)) / float(2))
        r = l + k
        sum = GFG.calculateSum(l, r - 1)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 3
        print(GFG.sumFibonacci(k))
