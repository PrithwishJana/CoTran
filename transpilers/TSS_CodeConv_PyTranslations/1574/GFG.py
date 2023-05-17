import math

class GFG:
    @staticmethod
    def Odd_Sum(n):
        total = math.trunc((n + 1) / float(2))
        odd = total * total
        return odd
    @staticmethod
    def Even_Sum(n):
        total = math.trunc((n) / float(2))
        even = total * (total + 1)
        return even
    @staticmethod
    def sumLtoR(L, R):
        odd_sum = 0
        even_sum = 0
        odd_sum = GFG.Odd_Sum(R) - GFG.Odd_Sum(L - 1)
        even_sum = GFG.Even_Sum(R) - GFG.Even_Sum(L - 1)
        return even_sum - odd_sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 1
        R = 5
        print(GFG.sumLtoR(L, R))
