import math

class p121:
    @staticmethod
    def main(args):
        print((p121()).run())
    _TURNS = 15
    def run(self):
        ways = [[] for _ in range(p121._TURNS + 1)]
        ways [0] = [java.math.BigInteger.ONE]
        for i in range(1, p121._TURNS + 1):
            ways [i] = [None for _ in range(i + 1)]
            for j in range(0, i + 1):
                temp = java.math.BigInteger.ZERO
                if j < i:
                    temp = ways [i - 1][j].multiply(java.math.BigInteger.valueOf(i))
                if j > 0:
                    temp = temp.add(ways [i - 1][j - 1])
                ways [i][j] = temp
        numer = java.math.BigInteger.ZERO
        for i in range(math.trunc(p121._TURNS / float(2)) + 1, p121._TURNS + 1):
            numer = numer.add(ways [p121._TURNS][i])
        denom = Library.factorial(p121._TURNS + 1)
        return str(denom.divide(numer))
