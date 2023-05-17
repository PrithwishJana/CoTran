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
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findPrime(n):
        num = n + 1
        while num > 0:
            if GFG.isPrime(num):
                return num
            num = num + 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minNumber(arr, n):
        sum = 0
        for i in range(0, n):
            sum += arr [i]
        if GFG.isPrime(sum):
            return 0
        num = GFG.findPrime(sum)
        return num - sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 4, 6, 8, 12]
        n = len(arr)
        print(GFG.minNumber(arr, n))
