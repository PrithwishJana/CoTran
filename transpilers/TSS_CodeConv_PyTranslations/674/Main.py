import math

class Squares:
    @staticmethod
    def numberOfSquares(base):
        base = (base - 2)
        base = math.trunc(base / float(2))
        return math.trunc(base * (base + 1) / float(2))
    @staticmethod
    def main(args):
        base = 8
        print(Squares.numberOfSquares(base))
