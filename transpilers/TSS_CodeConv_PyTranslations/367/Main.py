import math

class Circular:
    @staticmethod
    def removeAlternate(n):
        if n == 1:
            return 1
        if math.fmod(n, 2) == 0:
            return 2 * Circular.removeAlternate(math.trunc(n / float(2))) - 1
        else:
            return 2 * Circular.removeAlternate((math.trunc((n - 1) / float(2)))) + 1
    @staticmethod
    def main(args):
        n = 5
        print(Circular.removeAlternate(n), end = '')
        n = 10
        print("\n" + str(Circular.removeAlternate(n)), end = '')
