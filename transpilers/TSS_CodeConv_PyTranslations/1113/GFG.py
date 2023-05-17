class GFG:
    @staticmethod
    def ProdOfPrimes(n):
        prime = [False for _ in range(n + 1)]
        Arrays.fill(prime, True)
        p = 2
        while p * p <= n:
            if prime [p] == True:
                for i in range(p * 2, n + 1, p):
                    prime [i] = False
            p += 1
        prod = 1
        for i in range(2, n + 1):
            if prime [i]:
                prod *= i
        return prod
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        print(GFG.ProdOfPrimes(n), end = '')
