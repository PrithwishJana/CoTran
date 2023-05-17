import math

class GFG:
    @staticmethod
    def nDigitPerfectSquares(n):
        smallest = int(math.ceil(math.sqrt(10 ** (n - 1)))) ** 2
        print(str(smallest) + " ", end = '')
        largest = int((math.ceil(math.sqrt(10 ** n)) - 1)) ** 2
        print(largest, end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        GFG.nDigitPerfectSquares(n)
