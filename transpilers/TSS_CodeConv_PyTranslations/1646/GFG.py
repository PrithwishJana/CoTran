import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n, i):
        if n <= 2:
            return True if (n == 2) else False
        if math.fmod(n, i) == 0:
            return False
        if i * i > n:
            return True
        return GFG.isPrime(n, i + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        if GFG.isPrime(n, 2):
            print("Yes")
        else:
            print("No")
