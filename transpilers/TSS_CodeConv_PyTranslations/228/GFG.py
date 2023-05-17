import math

class GFG:
    @staticmethod
    def findLargest(arr, n):
        gcd = 0
        for i in range(0, n):
            gcd = GFG.__gcd(arr [i], gcd)
        return gcd
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        return a if b == 0 else GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 6, 9]
        n = len(arr)
        print(GFG.findLargest(arr, n))
