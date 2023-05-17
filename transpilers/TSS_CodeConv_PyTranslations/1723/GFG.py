import math

class GFG:
    @staticmethod
    def cntSubArr(arr, n):
        ans = 0
        for i in range(0, n):
            curr_gcd = 0
            for j in range(i, n):
                curr_gcd = GFG.__gcd(curr_gcd, arr [j])
                ans += 1 if (curr_gcd == 1) else 0
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if b == 0:
            return a
        return GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 1, 1]
        n = len(arr)
        print(GFG.cntSubArr(arr, n))
