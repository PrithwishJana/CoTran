import math

class GFG:
    @staticmethod
    def getsum(x):
        return math.trunc((x * (x + 1)) / float(2))
    @staticmethod
    def countJumps(n):
        n = abs(n)
        ans = 0
        while GFG.getsum(ans) < n or ((GFG.getsum(ans) - n) & 1) > 0:
            ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 9
        print(GFG.countJumps(n))
