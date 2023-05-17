import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        if n <= 1:
            return False
        i = 2
        while i <= math.sqrt(n):
            if math.fmod(n, i) == 0:
                return False
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPossible(N):
        if GFG.isPrime(N) and GFG.isPrime(N - 2):
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 13
        if GFG.isPossible(n) == True:
            print("Yes")
        else:
            print("No")
