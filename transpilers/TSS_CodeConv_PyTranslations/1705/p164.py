import math

class p164:
    @staticmethod
    def main(args):
        print((p164()).run())
    _BASE = 10
    _DIGITS = 20
    _CONSECUTIVE = 3
    _MAX_SUM = 9
    def run(self):
        ways = [[None for _ in range(Library.pow(p164._BASE, p164._CONSECUTIVE))] for _ in range(p164._DIGITS + p164._CONSECUTIVE + 1)]
        ways [0][0] = java.math.BigInteger.ONE
        prefix = 1
        while prefix < len(ways [0]):
            ways [0][prefix] = java.math.BigInteger.ZERO
            prefix += 1
        digits = 1
        while digits < len(ways):
            prefix = 0
            while prefix < len(ways [digits]):
                sum = java.math.BigInteger.ZERO
                if p164._digitSum(prefix) <= p164._MAX_SUM:
                    for nextDigit in range(0, p164._BASE):
                        sum = sum.add(ways [digits - 1][math.fmod(prefix, Library.pow(p164._BASE, p164._CONSECUTIVE - 1) * p164._BASE) + nextDigit])
                ways [digits][prefix] = sum
                prefix += 1
            digits += 1
        return str(ways [p164._DIGITS + p164._CONSECUTIVE][0].subtract(ways [p164._DIGITS + p164._CONSECUTIVE - 1][0]))
    @staticmethod
    def _digitSum(n):
        sum = 0
        while n != 0:
            sum += math.fmod(n, 10)
            n = math.trunc(n / float(10))
        return sum
