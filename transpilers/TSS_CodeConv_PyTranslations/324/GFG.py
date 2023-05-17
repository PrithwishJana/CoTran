class GFG:
    @staticmethod
    def numbersWith3Divisors(n):
        prime = [False for _ in range(n + 1)]
        Arrays.fill(prime, True)
        prime [0] = prime [1] = False
        p = 2
        while p * p <= n:
            if prime [p] == True:
                for i in range(p * 2, n + 1, p):
                    prime [i] = False
            p += 1
        print("Numbers with 3 divisors :")
        i = 0
        while i * i <= n:
            if prime [i]:
                print(str(i * i) + " ", end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 96
        GFG.numbersWith3Divisors(n)
