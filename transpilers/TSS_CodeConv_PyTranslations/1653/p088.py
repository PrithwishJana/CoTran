import math

class p088:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._minSumProduct = None

    @staticmethod
    def main(args):
        print((p088()).run())
    _LIMIT = 12000
    def run(self):
        self._minSumProduct = [0 for _ in range(p088._LIMIT + 1)]
        Arrays.fill(self._minSumProduct, Integer.MAX_VALUE)
        i = 2
        while i <= p088._LIMIT * 2:
            self._factorize(i, i, i, 0, 0)
            i += 1
        items = java.util.HashSet()
        i = 2
        while i < len(self._minSumProduct):
            items.add(self._minSumProduct [i])
            i += 1
        sum = 0
        for n in items:
            sum += n
        return str(sum)
    def _factorize(self, n, remain, maxFactor, sum, terms):
        if remain == 1:
            if sum > n:
                raise AssertionError()
            terms += n - sum
            if terms <= p088._LIMIT and n < self._minSumProduct [terms]:
                self._minSumProduct [terms] = n
        else:
            for i in range(2, maxFactor + 1):
                if math.fmod(remain, i) == 0:
                    factor = i
                    self._factorize(n, math.trunc(remain / float(factor)), min(factor, maxFactor), sum + factor, terms + 1)
