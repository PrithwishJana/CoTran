import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
    def powGCD(a, n, b):
        for i in range(0, n):
            a = a * a
        return GFG.gcd(a, b)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 10
        b = 5
        n = 2
        print(GFG.powGCD(a, n, b))
