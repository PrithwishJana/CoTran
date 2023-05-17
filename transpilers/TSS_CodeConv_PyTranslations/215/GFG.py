import math

class GFG:
    N = 1000005
    prime = [False for _ in range(N)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        Arrays.fill(GFG.prime, True)
        GFG.prime [1] = False
        GFG.prime [0] = False
        i = 2
        while i < GFG.N:
            if GFG.prime [i]:
                j = i * 2
                while j < GFG.N:
                    GFG.prime [j] = False
                    j += i
            i += 1
    @staticmethod
    def sumTruncatablePrimes(n):
        sum = 0
        for i in range(2, n):
            num = i
            flag = True
            while num > 0:
                if not GFG.prime [num]:
                    flag = False
                    break
                num = math.trunc(num / float(10))
            num = i
            power = 10
            while math.trunc(num / float(power)) > 0:
                if not GFG.prime [math.fmod(num, power)]:
                    flag = False
                    break
                power *= 10
            if flag:
                sum += i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 25
        GFG.sieve()
        print(GFG.sumTruncatablePrimes(n))
