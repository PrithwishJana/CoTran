import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def find(dividend, divisor, start, end):
        if start > end:
            return [0, dividend]
        mid = start + math.trunc((end - start) / float(2))
        n = dividend - divisor * mid
        if n > divisor:
            start = mid + 1
        elif n < 0:
            end = mid - 1
        else:
            if n == divisor:
                mid += 1
                n = 0
            return [mid, n]
        return GFG.find(dividend, divisor, start, end)
    @staticmethod
    def divide(dividend, divisor):
        return GFG.find(dividend, divisor, 1, dividend)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        dividend = 10
        divisor = 3
        ans = GFG.divide(dividend, divisor)
        print(str(ans [0]) + ", ", end = '')
        print(str(ans [1]) + "\n", end = '')
