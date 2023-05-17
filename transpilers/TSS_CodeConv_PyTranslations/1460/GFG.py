class GFG:
    @staticmethod
    def findEquation(a, b):
        sum = (a + b)
        product = (a * b)
        print("x^2 - (" + str(sum) + "x) + (" + str(product) + ") = 0")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 3
        GFG.findEquation(a, b)
