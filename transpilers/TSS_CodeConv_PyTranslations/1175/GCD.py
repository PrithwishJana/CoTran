import math

class GCD:
    @staticmethod
    def totalPrimeFactors(n):
        count = 0
        if (math.fmod(n, 2) == 0):
            count += 1
            while (math.fmod(n, 2) == 0):
                n = math.trunc(n / float(2))
        i = 3
        while i * i <= n:
            if (math.fmod(n, i) == 0):
                count += 1
            while (math.fmod(n, i) == 0):
                n = math.trunc(n / float(2))
            i = i + 2
        if n > 2:
            count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(G, L):
        if math.fmod(L, G) != 0:
            return 0
        div = math.trunc(L / float(G))
        return (1 << GCD.totalPrimeFactors(div))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        G = 2
        L = 12
        print("Total possible pair with GCD " + str(G), end = '')
        print(" & LCM " + str(L), end = '')
        print(" = " + str(GCD.countPairs(G, L)), end = '')
