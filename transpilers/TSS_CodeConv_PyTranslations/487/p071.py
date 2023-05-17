import math

class p071:
    @staticmethod
    def main(args):
        print((p071()).run())
    _LIMIT = 1000000
    def run(self):
        maxN = 0
        maxD = 1
        for d in range(1, p071._LIMIT + 1):
            n = math.trunc(d * 3 / float(7))
            if math.fmod(d, 7) == 0:
                n -= 1
            if int(n) * maxD > int(maxN) * d:
                maxN = n
                maxD = d
        return str(maxN)
