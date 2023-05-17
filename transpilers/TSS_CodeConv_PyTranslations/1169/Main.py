import math

class Solution:
    @staticmethod
    def closestMultiple(n, x):
        if x > n:
            return x
        n = n + math.trunc(x / float(2))
        n = n - (math.fmod(n, x))
        return n
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 56287
        x = 27
        print(Solution.closestMultiple(n, x))
