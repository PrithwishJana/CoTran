import math

class GFG:
    MAX = 1005
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes(primes):
        prime = [False for _ in range(GFG.MAX)]
        i = 0
        while i < len(prime):
            prime [i] = True
            i += 1
        p = 2
        while p * p < GFG.MAX:
            if prime [p] == True:
                i = p * 2
                while i < GFG.MAX:
                    prime [i] = False
                    i += p
            p += 1
        p = 2
        while p < GFG.MAX:
            if prime [p]:
                primes.insert(len(primes), p)
            p += 1
    @staticmethod
    def minimumSquareFreeDivisors(N):
        primes = []
        GFG.SieveOfEratosthenes(primes)
        max_count = 0
        i = 0
        while i < len(primes) and primes[i] * primes[i] <= N:
            if math.fmod(N, primes[i]) == 0:
                tmp = 0
                while math.fmod(N, primes[i]) == 0:
                    tmp += 1
                    N = math.trunc(N / float(primes[i]))
                max_count = max(max_count, tmp)
            i += 1
        if max_count == 0:
            max_count = 1
        return max_count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 24
        print("Minimum Number of Square Free Divisors is " + str(GFG.minimumSquareFreeDivisors(N)))
        N = 6
        print("Minimum Number of Square Free Divisors is " + str(GFG.minimumSquareFreeDivisors(N)))
