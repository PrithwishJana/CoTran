import math

class GFG:
    @staticmethod
    def calcFunction(n, r):
        finalDenominator = 1
        mx = max(r, n - r)
        for i in range(mx + 1, n + 1):
            denominator = int(i) ** i
            numerator = int((i - mx)) ** (i - mx)
            finalDenominator = math.trunc((finalDenominator * denominator) / float(numerator))
        return finalDenominator
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        r = 2
        print("1/" + str(GFG.calcFunction(n, r)))
