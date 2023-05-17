import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nthTerm(n):
        nth = 0
        if math.fmod(n, 2) == 0:
            nth = 2 * ((n * n) - n)
        else:
            nth = (2 * n * n) - n
        return nth
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 0
        n = 5
        print(GFG.nthTerm(n))
        n = 25
        print(GFG.nthTerm(n))
        n = 25000000
        print(GFG.nthTerm(n))
        n = 250000007
        print(GFG.nthTerm(n))
