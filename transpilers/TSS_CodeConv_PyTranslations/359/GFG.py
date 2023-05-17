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
    def nthElement(a, b, n):
        lcm = math.trunc((a * b) / float(GFG.__gcd(a, b)))
        l = 1
        r = min(a, b) * n
        while l <= r:
            mid = (l + r) >> 1
            val = math.trunc(mid / float(a)) + math.trunc(mid / float(b)) - math.trunc(mid / float(lcm))
            if val == n:
                return max((math.trunc(mid / float(a))) * a, (math.trunc(mid / float(b))) * b)
            if val < n:
                l = mid + 1
            else:
                r = mid - 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 5
        b = 3
        n = 5
        print(GFG.nthElement(a, b, n))
