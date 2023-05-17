import math

class GfG:
    @staticmethod
    def _findX(n, k):
        r = n
        v = 0
        u = 0
        m = int(math.sqrt(k)) + 1
        i = 2
        while i <= m and k > 1:
            if i == m:
                i = k
            u = v = 0
            while math.fmod(k, i) == 0:
                k = math.trunc(k / float(i))
                v += 1
            if v > 0:
                t = n
                while t > 0:
                    t = math.trunc(t / float(i))
                    u += t
                r = min(r, math.trunc(u / float(v)))
            i += 1
        return r
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        k = 2
        print(GfG._findX(n, k))
