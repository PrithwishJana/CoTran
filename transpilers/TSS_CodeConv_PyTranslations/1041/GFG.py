import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def bit(x):
        ans = 0
        while x > 0:
            x = math.trunc(x / float(2))
            ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(d, x):
        if GFG.bit(math.trunc(x / float(d))) <= GFG.bit(d):
            return True
        return False
    @staticmethod
    def bs(n):
        l = 1
        r = int(math.sqrt(n))
        while l < r:
            m = math.trunc((l + r) / float(2))
            if GFG.check(m, n):
                r = m
            else:
                l = m + 1
        if not GFG.check(l, n):
            return l + 1
        else:
            return l
    @staticmethod
    def countDivisor(n):
        return n - GFG.bs(n) + 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print(GFG.countDivisor(n))
