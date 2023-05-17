import math

class GFG:
    MAX = 1000000
    prime = [False for _ in range(MAX + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        GFG.prime [1] = True
        GFG.prime [0] = True
        p = 2
        while p * p <= GFG.MAX:
            if GFG.prime [p] == False:
                i = p * 2
                while i <= GFG.MAX:
                    GFG.prime [i] = True
                    i += p
            p += 1
    @staticmethod
    def productOfKthPrimes(arr, n, k):
        c = 0
        product = 1
        for i in range(0, n):
            if not GFG.prime [arr [i]]:
                c += 1
                if math.fmod(c, k) == 0:
                    product *= arr [i]
                    c = 0
        print(product)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        n = 5
        k = 2
        arr = [2, 3, 5, 7, 11]
        GFG.productOfKthPrimes(arr, n, k)
