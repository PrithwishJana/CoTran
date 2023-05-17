class GFG:
    @staticmethod
    def diff(n, mid):
        if n > (mid * mid * mid):
            return (n - (mid * mid * mid))
        else:
            return ((mid * mid * mid) - n)
    @staticmethod
    def cubicRoot(n):
        start = 0
        end = n
        e = 0.0000001
        while True:
            mid = (start + end) / 2
            error = GFG.diff(n, mid)
            if error <= e:
                return mid
            if (mid * mid * mid) > n:
                end = mid
            else:
                start = mid
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print("Cubic root of " + str(n) + " is " + str(GFG.cubicRoot(n)))
