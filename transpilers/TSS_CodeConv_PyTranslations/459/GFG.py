import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        flag = 1
        i = 2
        while i * i <= n:
            if math.fmod(n, i) == 0:
                flag = 0
                break
            i += 1
        return (True if flag == 1 else False)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPerfectSquare(x):
        sr = math.sqrt(x)
        return ((sr - math.floor(sr)) == 0)
    @staticmethod
    def countInterestingPrimes(n):
        answer = 0
        for i in range(2, n + 1):
            if GFG.isPrime(i):
                j = 1
                while j * j * j * j <= i:
                    if GFG.isPerfectSquare(i - j * j * j * j):
                        answer += 1
                        break
                    j += 1
        return answer
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 10
        print(GFG.countInterestingPrimes(N), end = '')
