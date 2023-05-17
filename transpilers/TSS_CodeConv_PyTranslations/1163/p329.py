class p329:
    @staticmethod
    def main(args):
        print((p329()).run())
    _START_NUM = 1
    _END_NUM = 500
    _CROAK_SEQ = "PPPPNNPPPNPPNPN"
    @staticmethod
    def _static_initializer():
        assert 0 <= p329._START_NUM and p329._START_NUM < p329._END_NUM and p329._END_NUM < Integer.MAX_VALUE
        assert 1 <= len(p329._CROAK_SEQ) and len(p329._CROAK_SEQ) <= 31

    _static_initializer()
    _NUM_JUMPS = len(_CROAK_SEQ) - 1
    _NUM_TRIALS = 1 << _NUM_JUMPS
    def run(self):
        globalNumerator = 0
        isPrime = Library.listPrimality(p329._END_NUM)
        for i in range(p329._START_NUM, p329._END_NUM + 1):
            for j in range(0, p329._NUM_TRIALS):
                pos = i
                trialNumerator = 1
                if isPrime [pos] == (p329._CROAK_SEQ[0] == 'P'):
                    trialNumerator *= 2
                for k in range(0, p329._NUM_JUMPS):
                    if pos <= p329._START_NUM:
                        pos += 1
                    elif pos >= p329._END_NUM:
                        pos -= 1
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java's unsigned right shift operator:
                    elif ((j >>> k) & 1) == 0:
                        pos += 1
                    else:
                        pos -= 1
                    if isPrime [pos] == (p329._CROAK_SEQ[k + 1] == 'P'):
                        trialNumerator *= 2
                globalNumerator += trialNumerator
        globalDenominator = java.math.BigInteger.valueOf(p329._END_NUM + 1 - p329._START_NUM).shiftLeft(p329._NUM_JUMPS).multiply(java.math.BigInteger.valueOf(3).pow(len(p329._CROAK_SEQ)))
        return str((Fraction(java.math.BigInteger.valueOf(globalNumerator), globalDenominator)))
