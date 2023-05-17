import math

class p142:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._isSquare = None

    @staticmethod
    def main(args):
        print((p142()).run())
    def run(self):
        sumLimit = 10
        while True:
            self._isSquare = [False for _ in range(sumLimit)]
            i = 0
            while i * i < sumLimit:
                self._isSquare [i * i] = True
                i += 1
            sum = self._findSum(sumLimit)
            if sum != - 1:
                sum = sumLimit
                break
            sumLimit *= 10
        while True:
            sum = self._findSum(sumLimit)
            if sum == - 1:
                return str(sumLimit)
            sumLimit = sum
    def _findSum(self, limit):
        a = 1
        while a * a < limit:
            for b in range(a - 1, 0, -1):
                if math.fmod((a + b), 2) != 0:
                    continue
                x = math.trunc((a * a + b * b) / float(2))
                y = math.trunc((a * a - b * b) / float(2))
                if x + y + 1 >= limit:
                    continue
                zlimit = min(y, limit - x - y)
                c = Library.sqrt(y) + 1
                while c * c - y < zlimit:
                    z = c * c - y
                    if self._isSquare [x + z] and self._isSquare [x - z] and self._isSquare [y - z]:
                        return x + y + z
                    c += 1
            a += 1
        return - 1
