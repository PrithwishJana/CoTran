import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def gcd(a, b):
        if a == 0:
            return b
        return GFG.gcd(math.fmod(b, a), a)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNumber(arr, n):
        ans = arr [0]
        for i in range(0, n):
            ans = GFG.gcd(ans, arr [i])
        for i in range(0, n):
            if arr [i] == ans:
                return ans
        return - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 2, 4]
        n = len(arr)
        print(GFG.findNumber(arr, n))
