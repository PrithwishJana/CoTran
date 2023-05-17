import math

class GFG:
    @staticmethod
    def sieveOfEratosthenes(N, s):
        prime = [False for _ in range(N + 1)]
        for i in range(2, N + 1, 2):
            s [i] = 2
        for i in range(3, N + 1, 2):
            if prime [i] == False:
                s [i] = i
                j = i
                while j * i <= N:
                    if prime [i * j] == False:
                        prime [i * j] = True
                        s [i * j] = i
                    j += 2
    @staticmethod
    def generatePrimeFactors(N):
        s = [0 for _ in range(N + 1)]
        GFG.sieveOfEratosthenes(N, s)
        print("Factor Power")
        curr = s [N]
        cnt = 1
        while N > 1:
            N = math.trunc(N / float(s [N]))
            if curr == s [N]:
                cnt += 1
                continue
            print(str(curr) + "\t" + str(cnt))
            curr = s [N]
            cnt = 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 360
        GFG.generatePrimeFactors(N)
