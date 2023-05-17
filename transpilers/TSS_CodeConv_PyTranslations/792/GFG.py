import math

class GFG:
    @staticmethod
    def divSum(n):
        sum = 1
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                sum = sum + i + math.trunc(n / float(i))
            i += 1
        return sum
    @staticmethod
    def areEquivalent(num1, num2):
        return GFG.divSum(num1) == GFG.divSum(num2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num1 = 559
        num2 = 703
        if GFG.areEquivalent(num1, num2):
            print("Equivalent")
        else:
            print("Not Equivalent")
