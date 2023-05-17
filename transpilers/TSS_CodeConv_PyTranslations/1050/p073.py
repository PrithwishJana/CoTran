class p073:
    @staticmethod
    def main(args):
        print((p073()).run())
    def run(self):
        return str(p073._sternBrocotCount(1, 3, 1, 2))
    @staticmethod
    def _sternBrocotCount(leftN, leftD, rightN, rightD):
        n = leftN + rightN
        d = leftD + rightD
        if d > 12000:
            return 0
        else:
            return 1 + p073._sternBrocotCount(leftN, leftD, n, d) + p073._sternBrocotCount(n, d, rightN, rightD)
