import math

class GCD:
    @staticmethod
    def gcd(a, b):
        if a == 0:
            return b
        return GCD.gcd(math.fmod(b, a), a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(G, L):
        count = 0
        p = G * L
        for a in range(1, L + 1):
            if (math.fmod(p, a) == 0) and GCD.gcd(a, math.trunc(p / float(a))) == G:
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        G = 2
        L = 12
        print("Total possible pair with GCD " + str(G), end = '')
        print(" & LCM " + str(L), end = '')
        print(" = " + str(GCD.countPairs(G, L)), end = '')
