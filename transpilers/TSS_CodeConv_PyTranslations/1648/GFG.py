import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(x):
        i = 2
        while i * i <= x:
            if math.fmod(x, i) == 0:
                return False
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minimumCost(n):
        if GFG.isPrime(n):
            return 1
        if math.fmod(n, 2) == 1 and GFG.isPrime(n - 2):
            return 2
        if math.fmod(n, 2) == 0:
            return 2
        return 3
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        print(GFG.minimumCost(n))
