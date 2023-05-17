import math

class JohnyLikesNumbers:
    @staticmethod
    def main(args):
        input = java.util.Scanner(System.in)
        n = input.nextInt()
        k = input.nextInt()
        pass
        print((math.trunc(n / float(k)) + 1) * k)
