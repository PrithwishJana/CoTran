import math

class p074:
    @staticmethod
    def main(args):
        print((p074()).run())
    _LIMIT = Library.pow(10, 6)
    def run(self):
        count = 0
        for i in range(0, p074._LIMIT):
            if p074._getChainLength(i) == 60:
                count += 1
        return str(count)
    @staticmethod
    def _getChainLength(n):
        seen = java.util.HashSet()
        while True:
            if not seen.add(n):
                return seen.size()
            n = p074._factorialize(n)
    _FACTORIAL = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    @staticmethod
    def _factorialize(n):
        sum = 0
        while n != 0:
            sum += p074._FACTORIAL [math.fmod(n, 10)]
            n = math.trunc(n / float(10))
        return sum
