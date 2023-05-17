class p087:
    @staticmethod
    def main(args):
        print((p087()).run())
    _LIMIT = 50000000
    def run(self):
        primes = Library.listPrimes(Library.sqrt(p087._LIMIT))
        sums = java.util.HashSet()
        sums.add(0)
        for i in range(2, 5):
            newsums = java.util.HashSet()
            for p in primes:
                q = 1
                for j in range(0, i):
                    q *= p
                if q > p087._LIMIT:
                    break
                r = int(q)
                for x in sums:
                    if x + r <= p087._LIMIT:
                        newsums.add(x + r)
            sums = newsums
        return str(sums.size())
