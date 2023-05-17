class p090:
    @staticmethod
    def main(args):
        print((p090()).run())
    def run(self):
        count = 0
        i = 0
        while i < (1 << 10):
            j = i
            while j < (1 << 10):
                if Integer.bitCount(i) == 6 and Integer.bitCount(j) == 6 and p090._isArrangementValid(i, j):
                    count += 1
                j += 1
            i += 1
        return str(count)
    _SQUARES = [[ 0, 1 ], [ 0, 4 ], [ 0, 9 ], [ 1, 6 ], [ 2, 5 ], [ 3, 6 ], [ 4, 9 ], [ 6, 4 ], [ 8, 1 ]]
    @staticmethod
    def _isArrangementValid(a, b):
        if p090._testBit(a, 6) or p090._testBit(a, 9):
            a |= (1 << 6) | (1 << 9)
        if p090._testBit(b, 6) or p090._testBit(b, 9):
            b |= (1 << 6) | (1 << 9)
        for sqr in p090._SQUARES:
            if not(p090._testBit(a, sqr [0]) and p090._testBit(b, sqr [1]) or p090._testBit(a, sqr [1]) and p090._testBit(b, sqr [0])):
                return False
        return True
    @staticmethod
    def _testBit(x, i):
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java's unsigned right shift operator:
        return ((x >>> i) & 1) != 0
