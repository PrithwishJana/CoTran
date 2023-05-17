import math

class GFG:
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * GFG.factorial(n - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nCr(n, r):
        return math.trunc(GFG.factorial(n) / float(GFG.factorial(n - r) * GFG.factorial(r)))
    @staticmethod
    def NumberOfWays(n, x, y):
        return GFG.nCr(2 * n - x - y, n - x) * GFG.factorial(n) * GFG.factorial(n)
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.lang.Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        x = 4
        y = 2
        print(GFG.NumberOfWays(n, x, y))
