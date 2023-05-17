import math

class GFG:
    MAX = 1000
    f = [0 for _ in range(MAX)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fib(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return (GFG.f [n] := 1)
        if GFG.f [n] != 0:
            return GFG.f [n]
        k = 0
        if (n & 1) != 0:
            k = math.trunc((n + 1) / float(2))
        else:
            k = math.trunc(n / float(2))
        if (n & 1) != 0:
            GFG.f [n] = (GFG.fib(k) * GFG.fib(k) + GFG.fib(k - 1) * GFG.fib(k - 1))
        else:
            GFG.f [n] = (2 * GFG.fib(k - 1) + GFG.fib(k)) * GFG.fib(k)
        return GFG.f [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
    def findLCMFibonacci(a, b):
        return math.trunc((GFG.fib(a) * GFG.fib(b)) / float(GFG.fib(GFG.gcd(a, b))))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 3
        b = 12
        print(GFG.findLCMFibonacci(a, b))
