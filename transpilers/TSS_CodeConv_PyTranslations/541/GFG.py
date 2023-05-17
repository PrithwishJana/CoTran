import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if a == 0 or b == 0:
            return 0
        if a == b:
            return a
        if a > b:
            return GFG.__gcd(a - b, b)
        return GFG.__gcd(a, b - a)
    @staticmethod
    def findLCM(arr, n):
        lcm = arr [0]
        for i in range(1, n):
            lcm = math.trunc((lcm * arr [i]) / float(GFG.__gcd(arr [i], lcm)))
        return lcm
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countNumbers(arr, n, l, r):
        lcm = GFG.findLCM(arr, n)
        count = (math.trunc(r / float(lcm))) - (math.trunc((l - 1) / float(lcm)))
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 4, 2]
        n = len(arr)
        l = 1
        r = 10
        print(GFG.countNumbers(arr, n, l, r))
