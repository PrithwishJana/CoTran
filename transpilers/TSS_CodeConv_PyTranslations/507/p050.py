class p050:
    @staticmethod
    def main(args):
        print((p050()).run())
    _LIMIT = Library.pow(10, 6)
    def run(self):
        isPrime = Library.listPrimality(p050._LIMIT)
        primes = Library.listPrimes(p050._LIMIT)
        maxSum = 0
        maxRun = - 1
        i = 0
        while i < len(primes):
            sum = 0
            j = i
            while j < len(primes):
                sum += primes [j]
                if sum > p050._LIMIT:
                    break
                elif j - i > maxRun and sum > maxSum and isPrime [sum]:
                    maxSum = sum
                    maxRun = j - i
                j += 1
            i += 1
        return str(maxSum)
