import math

class GFG:
    @staticmethod
    def check_digits(n):
        while n != 0:
            if math.fmod((math.fmod(n, 10)), 2) != 0:
                return 0
            n = math.trunc(n / float(10))
        return 1
    @staticmethod
    def smallest_number(n):
        i = n
        while True:
            if GFG.check_digits(i) != 0:
                return i
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 2397
        print(GFG.smallest_number(N))
