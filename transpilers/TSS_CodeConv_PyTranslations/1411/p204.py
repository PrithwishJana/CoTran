class p204:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._primes = Library.listPrimes(100)

    @staticmethod
    def main(args):
        print((p204()).run())
    def run(self):
        return str(self._count(0, 1))
    _LIMIT = Library.pow(10, 9)
    def _count(self, primeIndex, product):
        if primeIndex == len(self._primes):
            return 1 if product <= p204._LIMIT else 0
        else:
            count = 0
            while product <= p204._LIMIT:
                count += self._count(primeIndex + 1, product)
                product *= self._primes [primeIndex]
            return count
