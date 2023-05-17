import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                return False
            i += 1
        return True
    @staticmethod
    def minimumSum(n):
        if GFG.isPrime(n):
            return 1
        if math.fmod(n, 2) == 0:
            return 2
        if GFG.isPrime(n - 2):
            return 2
        return 3
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 27
        print(GFG.minimumSum(n))
