import math

class p187:
    @staticmethod
    def main(args):
        print((p187()).run())
    _LIMIT = Library.pow(10, 8) - 1
    def run(self):
        count = 0
        primes = Library.listPrimes(math.trunc(p187._LIMIT / float(2)))
        i = 0
        sqrt = Library.sqrt(LIMIT)
        while i < len(primes) and primes [i] <= sqrt:
            end = java.util.Arrays.binarySearch(primes, math.trunc(p187._LIMIT / float(primes [i])))
            if end >= 0:
                end += 1
            else:
                end = - end - 1
            count += end - i
            i += 1
        return str(count)
