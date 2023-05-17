import math

class p092:
    @staticmethod
    def main(args):
        print((p092()).run())
    _LIMIT = Library.pow(10, 7)
    def run(self):
        count = 0
        for i in range(1, p092._LIMIT):
            if p092._isClass89(i):
                count += 1
        return str(count)
    @staticmethod
    def _isClass89(x):
        while True:
            if x == 1:
                return False
            elif x == 89:
                return True
            else:
                x = p092._nextNumber(x)
    @staticmethod
    def _nextNumber(x):
        sum = 0
        while x != 0:
            sum += (math.fmod(x, 10)) * (math.fmod(x, 10))
            x = math.trunc(x / float(10))
        return sum
