import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 10
        b = 15
        g = 0
        g = GFG.gcd(a, b)
        print("GCD(" + str(a) + " , " + str(b) + ") = " + str(g))
        a = 35
        b = 10
        g = GFG.gcd(a, b)
        print("GCD(" + str(a) + " , " + str(b) + ") = " + str(g))
        a = 31
        b = 2
        g = GFG.gcd(a, b)
        print("GCD(" + str(a) + " , " + str(b) + ") = " + str(g))
