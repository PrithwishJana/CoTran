import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
    def lcm(a, b):
        return math.trunc((a * b) / float(GFG.gcd(a, b)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(arr, n):
        ans = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                if GFG.lcm(arr [i], arr [j]) == GFG.gcd(arr [i], arr [j]):
                    ans += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 1]
        n = len(arr)
        print(GFG.countPairs(arr, n), end = '')
