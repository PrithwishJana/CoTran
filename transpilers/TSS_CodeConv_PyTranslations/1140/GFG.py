import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
    def largestGCD1Subset(A, n):
        currentGCD = A [0]
        for i in range(1, n):
            currentGCD = GFG.gcd(currentGCD, A [i])
            if currentGCD == 1:
                return n
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [2, 18, 6, 3]
        n = len(A)
        print(GFG.largestGCD1Subset(A, n))
