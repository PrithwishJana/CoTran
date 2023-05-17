import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if math.fmod(n, i) == 0:
                return False
        return True
    @staticmethod
    def countPrimePosition(arr):
        c0 = 0
        c1 = 0
        n = len(arr)
        for i in range(0, n):
            if arr [i] == 0 and GFG.isPrime(i):
                c0 += 1
            if arr [i] == 1 and GFG.isPrime(i):
                c1 += 1
        print("Number of 0s = " + str(c0))
        print("Number of 1s = " + str(c1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 0, 1, 0, 1]
        GFG.countPrimePosition(arr)
