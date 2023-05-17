import math

class GFG:
    MAX = 1000000
    prime = [False for _ in range(MAX + 1)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes():
        i = 0
        while i < len(GFG.prime):
            GFG.prime [i] = True
            i += 1
        GFG.prime [1] = False
        GFG.prime [0] = False
        p = 2
        while p * p <= GFG.MAX:
            if GFG.prime [p] == True:
                i = p * 2
                while i <= GFG.MAX:
                    GFG.prime [i] = False
                    i += p
            p += 1
    @staticmethod
    def SumOfKthPrimes(arr, n, k):
        c = 0
        sum = 0
        for i in range(0, n):
            if GFG.prime [arr [i]]:
                c += 1
                if math.fmod(c, k) == 0:
                    sum += arr [i]
                    c = 0
        print(sum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.SieveOfEratosthenes()
        arr = [2, 3, 5, 7, 11]
        n = len(arr)
        k = 2
        GFG.SumOfKthPrimes(arr, n, k)
