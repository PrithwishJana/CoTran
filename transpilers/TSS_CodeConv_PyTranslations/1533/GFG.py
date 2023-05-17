import math

class GFG:
    @staticmethod
    def maxPrimeFactors(n):
        maxPrime = - 1
        while math.fmod(n, 2) == 0:
            maxPrime = 2
            n >>= 1
        i = 3
        while i <= math.sqrt(n):
            while math.fmod(n, i) == 0:
                maxPrime = i
                n = math.trunc(n / float(i))
            i += 2
        if n > 2:
            maxPrime = n
        return maxPrime
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        print(GFG.maxPrimeFactors(n))
        n = 25698751364526
        print(GFG.maxPrimeFactors(n))
