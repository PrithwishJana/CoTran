import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(s, k):
        i = 0
        while i < len(s):
            if s[i] != s[math.fmod(i, k)]:
                return False
            i += 1
        return True
    @staticmethod
    def countCommonDivisors(a, b):
        ct = 0
        n = len(a)
        m = len(b)
        i = 1
        while i <= min(n, m):
            if math.fmod(n, i) == 0 and math.fmod(m, i) == 0:
                if a[0:i] is b[0:i]:
                    if GFG.check(a, i) and GFG.check(b, i):
                        ct += 1
            i += 1
        return ct
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = "xaxa"
        b = "xaxaxaxa"
        print(GFG.countCommonDivisors(a, b))
