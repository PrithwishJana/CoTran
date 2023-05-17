import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def SieveOfEratosthenes(n, isPrime):
        isPrime [0] = isPrime [1] = False
        for i in range(2, n + 1):
            isPrime [i] = True
        p = 2
        while p * p <= n:
            if isPrime [p] == True:
                for i in range(p * 2, n + 1, p):
                    isPrime [i] = False
            p += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findPrimePair(n):
        flag = 0
        isPrime = [False for _ in range(n + 1)]
        GFG.SieveOfEratosthenes(n, isPrime)
        for i in range(2, n):
            x = math.trunc(n / float(i))
            if isPrime [i] and isPrime [x] and x != i and x * i == n:
                print(str(i) + " " + str(x))
                flag = 1
                return
        if flag == 0:
            print("No such pair found")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 39
        GFG.findPrimePair(n)
