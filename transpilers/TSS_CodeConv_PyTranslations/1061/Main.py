import math

class Geeks:
    @staticmethod
    def check_digits(n):
        while n > 0:
            if math.fmod((math.fmod(n, 10)), 2) == 0:
                return 0
            n = math.trunc(n / float(10))
        return 1
    @staticmethod
    def smallest_number(n):
        i = n
        while True:
            if Geeks.check_digits(i) > 0:
                return i
            i += 1
    @staticmethod
    def main(args):
        N = 2397
        print(Geeks.smallest_number(N))
