import math

class GFG:
    @staticmethod
    def countPrimeFactors(n):
        count = 0
        while math.fmod(n, 2) == 0:
            n = math.trunc(n / float(2))
            count += 1
        i = 3
        while i <= math.sqrt(n):
            while math.fmod(n, i) == 0:
                n = math.trunc(n / float(i))
                count += 1
            i = i + 2
        if n > 2:
            count += 1
        return (count)
    @staticmethod
    def printKAlmostPrimes(k, n):
        i = 1
        num = 2
        while i <= n:
            if GFG.countPrimeFactors(num) == k:
                print(str(num) + " ", end = '')
                i += 1
            num += 1
        return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        k = 2
        print("First " + str(n) + " " + str(k) + "-almost prime numbers: ")
        GFG.printKAlmostPrimes(k, n)
