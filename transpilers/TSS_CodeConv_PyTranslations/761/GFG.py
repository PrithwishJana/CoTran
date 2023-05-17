import math

class GFG:
    MAXN = 100001
    prime = [False for _ in range(MAXN)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        i = 0
        while i < len(GFG.prime):
            GFG.prime [i] = True
            i += 1
        GFG.prime [0] = False
        GFG.prime [1] = False
        p = 2
        while p * p < GFG.MAXN:
            if GFG.prime [p] == True:
                for i in range(p * p, GFG.MAXN, p):
                    GFG.prime [i] = False
            p += 1
    @staticmethod
    def common_prime(a, b):
        gcd = int(GFG.__gcd(a, b))
        i = 2
        while i <= (gcd):
            if GFG.prime [i] and math.fmod(gcd, i) == 0:
                print(str(i) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if a == 0:
            return b
        return GFG.__gcd(math.fmod(b, a), a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        a = 6
        b = 12
        GFG.common_prime(a, b)
