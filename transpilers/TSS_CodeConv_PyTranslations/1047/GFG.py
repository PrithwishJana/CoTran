import math

class GFG:
    @staticmethod
    def nthXorFib(n, a, b):
        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return (a ^ b)
        return GFG.nthXorFib(math.fmod(n, 3), a, b)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 1
        b = 2
        n = 10
        print(GFG.nthXorFib(n, a, b))
