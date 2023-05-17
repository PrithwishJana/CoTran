import math

class Solution:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if a == b:
            return a
        if a > b:
            return Solution.__gcd(a - b, b)
        return Solution.__gcd(a, b - a)
    @staticmethod
    def lcm(a, b):
        return (math.trunc(a / float(Solution.__gcd(a, b) * b)))
    @staticmethod
    def getMinValue(c):
        ans = Integer.MAX_VALUE
        i = 1
        while i <= math.sqrt(c):
            if math.fmod(c, i) == 0 and Solution.lcm(i, math.trunc(c / float(i))) == c:
                ans = min(ans, max(i, math.trunc(c / float(i))))
            i += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        c = 6
        print(Solution.getMinValue(c))
