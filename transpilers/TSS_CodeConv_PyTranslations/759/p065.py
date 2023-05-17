import math

class p065:
    @staticmethod
    def main(args):
        print((p065()).run())
    def run(self):
        n = java.math.BigInteger.ONE
        d = java.math.BigInteger.ZERO
        for i in range(99, -1, -1):
            temp = java.math.BigInteger.valueOf(p065._continuedFractionTerm(i)).multiply(n).add(d)
            d = n
            n = temp
        sum = 0
        while n is not java.math.BigInteger.ZERO:
            divrem = n.divideAndRemainder(java.math.BigInteger.TEN)
            sum += divrem [1].intValue()
            n = divrem [0]
        return str(sum)
    @staticmethod
    def _continuedFractionTerm(i):
        if i == 0:
            return 2
        elif math.fmod(i, 3) == 2:
            return math.trunc(i / float(3 * 2)) + 2
        else:
            return 1
