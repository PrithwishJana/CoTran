import math

class GFG:
    @staticmethod
    def maxnumber(n, k):
        for j in range(0, k):
            ans = 0
            i = 1
            while math.trunc(n / float(i)) > 0:
                temp = (math.trunc(n / float(i * 10))) * i + (math.fmod(n, i))
                i *= 10
                ans = max(ans, temp)
            n = ans
        return n
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6358
        k = 1
        print(GFG.maxnumber(n, k))
