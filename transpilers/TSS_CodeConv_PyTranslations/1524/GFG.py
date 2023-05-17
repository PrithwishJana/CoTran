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
                for i in range(p * p, n + 1, p):
                    isPrime [i] = False
            p += 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findPrimePair(n):
        isPrime = [False for _ in range(n + 1)]
        GFG.SieveOfEratosthenes(n, isPrime)
        for i in range(0, n):
            if isPrime [i] and isPrime [n - i]:
                print(str(i) + " " + str(n - i), end = '')
                return
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 74
        GFG.findPrimePair(n)
