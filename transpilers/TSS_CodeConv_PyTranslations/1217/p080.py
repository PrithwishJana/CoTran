class p080:
    @staticmethod
    def main(args):
        print((p080()).run())
    def run(self):
        sum = 0
        for i in range(1, 101):
            x = java.math.BigInteger.valueOf(i)
            x = x.multiply(java.math.BigInteger.TEN.pow(100 * 2))
            y = p080._sqrt(x)
            if y.multiply(y) is not x:
                s = str(y).substring(0, 100)
                j = 0
                while j < len(s):
                    sum += s[j] - '0'
                    j += 1
        return str(sum)
    @staticmethod
    def _sqrt(x):
        i = 0
        while java.math.BigInteger.TEN.pow(i * 2).compareTo(x) <= 0:
            i += 1
        y = java.math.BigInteger.ZERO
        while i >= 0:
            j = 0
            delta = None
            for j in range(9, -1, -1):
                temp = java.math.BigInteger.valueOf(j).multiply(java.math.BigInteger.TEN.pow(i))
                delta = y.shiftLeft(1).add(temp).multiply(temp)
                if delta.compareTo(x) <= 0:
                    break
            if j < 0:
                raise AssertionError()
            x = x.subtract(delta)
            y = y.add(java.math.BigInteger.valueOf(j).multiply(java.math.BigInteger.TEN.pow(i)))
            i -= 1
        return y
