import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPrime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if math.fmod(n, 2) == 0 or math.fmod(n, 3) == 0:
            return False
        i = 5
        while i * i <= n:
            if math.fmod(n, i) == 0 or math.fmod(n, (i + 2)) == 0:
                return False
            i = i + 6
        return True
    @staticmethod
    def primeBitsInRange(l, r):
        tot_bit = 0
        count = 0
        for i in range(l, r + 1):
            tot_bit = Integer.bitCount(i)
            if GFG.isPrime(tot_bit):
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 6
        r = 10
        print(GFG.primeBitsInRange(l, r))
