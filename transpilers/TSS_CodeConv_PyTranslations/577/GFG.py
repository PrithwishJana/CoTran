import math

class GFG:
    @staticmethod
    def maxResult(n, a, b, c):
        maxVal = 0
        for i in range(0, n + 1, a):
            j = 0
            while j <= n - i:
                z = math.trunc((n - (i + j)) / float(c))
                if math.floor(z) == math.ceil(z):
                    x = math.trunc(i / float(a))
                    y = math.trunc(j / float(b))
                    maxVal = max(maxVal, x + y + int(z))
                j += b
        return maxVal
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        a = 5
        b = 3
        c = 4
        print(GFG.maxResult(n, a, b, c))
