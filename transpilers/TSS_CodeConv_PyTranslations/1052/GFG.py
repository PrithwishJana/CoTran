class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve(prime, n):
        prime [0] = False
        prime [1] = False
        p = 2
        while p * p <= n:
            if prime [p] == True:
                for i in range(p * p, n + 1, p):
                    prime [i] = False
            p += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sumPrime(d):
        i = 0
        maxVal = int(10) ** d - 1
        prime = [False for _ in range(maxVal + 1)]
        i = 0
        while i < maxVal + 1:
            prime [i] = True
            i += 1
        GFG.sieve(prime, maxVal)
        sum = 0
        for i in range(2, maxVal + 1):
            if prime [i]:
                sum += i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        d = 3
        print(GFG.sumPrime(d))
