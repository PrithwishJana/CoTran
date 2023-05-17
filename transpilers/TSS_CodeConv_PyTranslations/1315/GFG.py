import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(n, base):
        sum = 0
        while n > 0:
            remainder = math.fmod(n, base)
            sum += remainder
            n = math.trunc(n / float(base))
        return sum
    @staticmethod
    def SumsOfDigits(n):
        sum = 0
        base = 2
        while base <= math.trunc(n / float(2)):
            sum += GFG.solve(n, base)
            base += 1
        print(sum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 8
        GFG.SumsOfDigits(n)
