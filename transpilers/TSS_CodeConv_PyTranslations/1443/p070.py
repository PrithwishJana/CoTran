class p070:
    @staticmethod
    def main(args):
        print((p070()).run())
    _LIMIT = Library.pow(10, 7)
    def run(self):
        minNumer = 1
        minDenom = 0
        totients = Library.listTotients(p070._LIMIT - 1)
        n = 2
        while n < len(totients):
            tot = totients [n]
            if int(n) * minDenom < int(minNumer) * tot and p070._hasSameDigits(n, tot):
                minNumer = n
                minDenom = tot
            n += 1
        if minDenom == 0:
            raise RuntimeException("Not found")
        return str(minNumer)
    @staticmethod
    def _hasSameDigits(x, y):
        xdigits = str(x).toCharArray()
        ydigits = str(y).toCharArray()
        xdigits.sort()
        ydigits.sort()
        return java.util.Arrays.equals(xdigits, ydigits)
