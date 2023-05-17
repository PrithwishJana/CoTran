import math

class GFG:
    MAX = 50002
    primes = []
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        isPrime = [False for _ in range(GFG.MAX)]
        i = 0
        while i < GFG.MAX:
            isPrime [i] = True
            i += 1
        p = 2
        while p * p < GFG.MAX:
            if isPrime [p] == True:
                i = p * 2
                while i < GFG.MAX:
                    isPrime [i] = False
                    i += p
            p += 1
        p = 2
        while p < GFG.MAX:
            if isPrime [p] == True:
                GFG.primes.append(p)
            p += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def power(x, y):
        count = 0
        z = y
        while x >= z:
            count += (math.trunc(x / float(z)))
            z *= y
        return count
    @staticmethod
    def modMult(a, b, mod):
        res = 0
        a = math.fmod(a, mod)
        while b > 0:
            if math.fmod(b, 2) == 1:
                res = math.fmod((res + a), mod)
            a = math.fmod((a * 2), mod)
            b = math.trunc(b / float(2))
        return math.fmod(res, mod)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n, m):
        ans = 1
        for i in range(1, len(GFG.primes)):
            powers = GFG.power(n, GFG.primes[i])
            if powers == 0:
                break
            ans = math.fmod(GFG.modMult(ans, powers + 1, m), m)
        if (math.fmod((ans - 1), m)) < 0:
            return math.fmod((ans - 1 + m), m)
        else:
            return math.fmod((ans - 1), m)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.sieve()
        n = 4
        m = 7
        print(GFG.countWays(n, m))
