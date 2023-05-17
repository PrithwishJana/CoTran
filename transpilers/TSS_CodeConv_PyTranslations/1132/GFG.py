import math

class GFG:
    @staticmethod
    def discreteLogarithm(a, b, m):
        n = int((math.sqrt(m) + 1))
        an = 1
        for i in range(0, n):
            an = math.fmod((an * a), m)
        value = [0 for _ in range(m)]
        i = 1
        cur = an
        while i <= n:
            if value [cur] == 0:
                value [cur] = i
            cur = math.fmod((cur * an), m)
            i += 1
        i = 0
        cur = b
        while i <= n:
            if value [cur] > 0:
                ans = value [cur] * n - i
                if ans < m:
                    return ans
            cur = math.fmod((cur * a), m)
            i += 1
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 3
        m = 5
        print(GFG.discreteLogarithm(a, b, m))
        a = 3
        b = 7
        m = 11
        print(GFG.discreteLogarithm(a, b, m))
