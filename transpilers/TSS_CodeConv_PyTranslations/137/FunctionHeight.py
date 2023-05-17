import math

class FunctionHeight:
    @staticmethod
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextLong()
        k = sc.nextLong()
        print(1 if n >= k else (math.trunc(k / float(n)) if math.fmod(k, n) == 0 else (math.trunc(k / float(n)) + 1)))
