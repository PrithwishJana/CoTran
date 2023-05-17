import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countNumbers(L, R, K):
        if K == 9:
            K = 0
        totalnumbers = R - L + 1
        factor9 = math.trunc(totalnumbers / float(9))
        rem = math.fmod(totalnumbers, 9)
        ans = factor9
        i = R
        while i > R - rem:
            rem1 = math.fmod(i, 9)
            if rem1 == K:
                ans += 1
            i -= 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 10
        R = 22
        K = 3
        print(GFG.countNumbers(L, R, K))
