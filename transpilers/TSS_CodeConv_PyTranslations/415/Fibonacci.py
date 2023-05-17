import math

class Fibonacci:
    @staticmethod
    def findIndex(n):
        fibo = 2.078087F * float(math.log(n)) + 1.672276F
        return round(fibo)
    @staticmethod
    def main(args):
        n = 21
        print(Fibonacci.findIndex(n))
