class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sum(x, y, n):
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        sum1 = int(((x ** 2 * (x ** (2 * n) - 1)) / (x ** 2 - 1)))
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        sum2 = int(((x * y * (x ** n * y ** n - 1)) / (x * y - 1)))
        return sum1 + sum2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 2
        y = 2
        n = 2
        print(GFG.sum(x, y, n))
