class p243:
    @staticmethod
    def main(args):
        print((p243()).run())
    _TARGET = Fraction(java.math.BigInteger.valueOf(15499), java.math.BigInteger.valueOf(94744))
    def run(self):
        totient = java.math.BigInteger.ONE
        denominator = java.math.BigInteger.ONE
        p = 2
        while True:
            totient = totient.multiply(java.math.BigInteger.valueOf(p - 1))
            denominator = denominator.multiply(java.math.BigInteger.valueOf(p))
            loop_condition = True
            while loop_condition:
                p += 1
                loop_condition = not Library.isPrime(p)
            if (Fraction(totient, denominator)).compareTo(p243._TARGET) < 0:
                for i in range(1, p):
                    numer = java.math.BigInteger.valueOf(i).multiply(totient)
                    denom = java.math.BigInteger.valueOf(i).multiply(denominator)
                    if (Fraction(numer, denom.subtract(java.math.BigInteger.ONE))).compareTo(p243._TARGET) < 0:
                        return str(denom)
