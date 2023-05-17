import math

class GFG:
    MOD = 1000000007
    @staticmethod
    def mult(a, b):
        return math.fmod(((math.fmod(a, GFG.MOD)) * (math.fmod(b, GFG.MOD))), GFG.MOD)
    @staticmethod
    def calculate_factors(n):
        ans = 0
        cnt = 0
        cnt = 0
        ans = 1
        while math.fmod(n, 2) == 0:
            cnt += 1
            n = math.trunc(n / float(2))
        if math.fmod(cnt, 2) == 1:
            ans = GFG.mult(ans, (cnt + 1))
        i = 3
        while i <= math.sqrt(n):
            cnt = 0
            while math.fmod(n, i) == 0:
                cnt += 1
                n = math.trunc(n / float(i))
            if math.fmod(cnt, 2) == 1:
                ans = GFG.mult(ans, (cnt + 1))
            i += 2
        if n > 2:
            ans = GFG.mult(ans, (2))
        return math.fmod(ans, GFG.MOD)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 193748576239475639
        GFG.MOD = 17
        print(str(GFG.calculate_factors(n)) + "\n", end = '')
