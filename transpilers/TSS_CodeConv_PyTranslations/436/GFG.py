import math

class GFG:
    @staticmethod
    def nth_term(a, b, n):
        z = 0
        if math.fmod(n, 6) == 1:
            z = a
        elif math.fmod(n, 6) == 2:
            z = b
        elif math.fmod(n, 6) == 3:
            z = b - a
        elif math.fmod(n, 6) == 4:
            z = - a
        elif math.fmod(n, 6) == 5:
            z = - b
        if math.fmod(n, 6) == 0:
            z = - (b - a)
        return z
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 10
        b = 17
        n = 3
        print(GFG.nth_term(a, b, n))
