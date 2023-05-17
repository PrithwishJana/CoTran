import math

class p401:
    @staticmethod
    def main(args):
        print((p401()).run())
    _LIMIT = 1000000000000000
    _MODULUS = Library.pow(10, 9)
    def run(self):
        splitCount = int(Library.sqrt(p401._LIMIT))
        splitCount = max(math.trunc(splitCount / float(3)), 1)
        splitAt = int((math.trunc(p401._LIMIT / float(splitCount + 1))))
        sum = 0
        for i in range(1, splitAt + 1):
            count = math.trunc(p401._LIMIT / float(math.fmod(i, p401._MODULUS)))
            term = math.fmod(int(i) * i, p401._MODULUS)
            term = math.fmod(term * count, p401._MODULUS)
            sum = math.fmod((sum + term), p401._MODULUS)
        for i in range(splitCount, 0, -1):
            start = math.trunc(p401._LIMIT / float(i + 1))
            end = math.trunc(p401._LIMIT / float(i))
            sumSquares = p401._sumSquaresMod(end) - p401._sumSquaresMod(start)
            sumSquares = math.fmod((sumSquares + p401._MODULUS), p401._MODULUS)
            sum = math.fmod((sum + math.fmod(i * sumSquares, p401._MODULUS)), p401._MODULUS)
        return str(sum)
    _MODULUS_BI = java.math.BigInteger.valueOf(_MODULUS)
    _SIX_BI = java.math.BigInteger.valueOf(6)
    @staticmethod
    def _sumSquaresMod(n):
        x = java.math.BigInteger.valueOf(n)
        y = x.multiply(x.add(java.math.BigInteger.ONE))
        y = y.multiply(x.shiftLeft(1).add(java.math.BigInteger.ONE))
        y = y.divide(p401._SIX_BI)
        y = y.mod(p401._MODULUS_BI)
        return y.longValue()
