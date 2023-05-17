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
    def isThreeDisctFactors(n):
        sq = int(math.sqrt(n))
        if 1 * sq * sq != n:
            return False
        return True if GFG.isPrime(sq) else False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = 9
        if GFG.isThreeDisctFactors(num):
            print("Yes")
        else:
            print("No")
        num = 15
        if GFG.isThreeDisctFactors(num):
            print("Yes")
        else:
            print("No")
        num = 12397923568441
        if GFG.isThreeDisctFactors(num):
            print("Yes")
        else:
            print("No")
