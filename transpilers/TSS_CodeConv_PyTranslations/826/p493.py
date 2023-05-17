class p493:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._numerator = java.math.BigInteger.ZERO

    @staticmethod
    def main(args):
        print((p493()).run())
    _NUM_COLORS = 7
    _BALLS_PER_COLOR = 10
    _NUM_PICKED = 20
    def run(self):
        self._explore(p493._NUM_PICKED, p493._BALLS_PER_COLOR, java.util.Stack())
        denominator = Library.binomial(p493._NUM_COLORS * p493._BALLS_PER_COLOR, p493._NUM_PICKED)
        num = java.math.BigDecimal(self._numerator)
        den = java.math.BigDecimal(denominator)
        return str(num.divide(den, 9, java.math.RoundingMode.HALF_EVEN))
    def _explore(self, remain, limit, history):
        if remain == 0:
            hist = [0 for _ in range(p493._NUM_COLORS)]
            for i, unusedItem in enumerate(history):
                hist [i] = history.get(i)
            histogram = [0 for _ in range(p493._BALLS_PER_COLOR + 1)]
            for x in hist:
                histogram [x] += 1
            count = Library.factorial(p493._NUM_COLORS)
            for x in histogram:
                count = p493._divideExactly(count, Library.factorial(x))
            for x in hist:
                count = count.multiply(Library.binomial(p493._BALLS_PER_COLOR, x))
            distinctColors = history.size()
            self._numerator = self._numerator.add(count.multiply(java.math.BigInteger.valueOf(distinctColors)))
        elif history.size() < p493._NUM_COLORS:
            for i in range(min(limit, remain), 0, -1):
                history.push(i)
                self._explore(remain - i, i, history)
                history.pop()
    @staticmethod
    def _divideExactly(x, y):
        temp = x.divideAndRemainder(y)
        if temp [1].signum() != 0:
            raise IllegalArgumentException("Not divisible")
        return temp [0]
