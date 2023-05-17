import math

class GFG:
    @staticmethod
    def sumOfDigitsSingle(x):
        ans = 0
        while x != 0:
            ans += math.fmod(x, 10)
            x = math.trunc(x / float(10))
        return ans
    @staticmethod
    def closest(x):
        ans = 0
        while ans * 10 + 9 <= x:
            ans = ans * 10 + 9
        return ans
    @staticmethod
    def sumOfDigitsTwoParts(N):
        A = GFG.closest(N)
        return GFG.sumOfDigitsSingle(A) + GFG.sumOfDigitsSingle(N - A)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 35
        print(GFG.sumOfDigitsTwoParts(N), end = '')
