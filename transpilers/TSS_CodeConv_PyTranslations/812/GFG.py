import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(n):
        m = n
        while n != 0:
            r = math.fmod(n, 10)
            if r > 0:
                if (math.fmod(m, r)) != 0:
                    return False
            n = math.trunc(n / float(10))
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def count(l, r):
        ans = 0
        for i in range(l, r + 1):
            if GFG.check(i):
                ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 10
        r = 20
        print(GFG.count(10, 20))
