import math

class Solution:
    res = 0
    @staticmethod
    def checkRecursive(num, x, k, n):
        if x == 0:
            Solution.res += 1
        r = int(math.floor(num ** (1.0 / n)))
        for i in range(k + 1, r + 1):
            a = x - int(i) ** n
            if a >= 0:
                Solution.checkRecursive(num, x - int(i) ** n, i, n)
        return Solution.res
    @staticmethod
    def check(x, n):
        return Solution.checkRecursive(x, x, 0, n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(Solution.check(10, 2))
