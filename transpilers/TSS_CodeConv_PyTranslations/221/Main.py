import math

class Eulerian:
    @staticmethod
    def precisionCompute(x, y, n):
        if y == 0:
            print("Infinite", end = '')
            return
        if x == 0:
            print("0", end = '')
            return
        if n <= 0:
            print(math.trunc(x / float(y)), end = '')
            return
        if ((x > 0) and (y < 0)) or ((x < 0) and (y > 0)):
            print("-", end = '')
            x = x if x > 0 else - x
            y = y if y > 0 else - y
        d = math.trunc(x / float(y))
        for i in range(0, n + 1):
            print(d, end = '')
            x = x - (y * d)
            if x == 0:
                break
            x = x * 10
            d = math.trunc(x / float(y))
            if i == 0:
                print(".", end = '')
    @staticmethod
    def main(args):
        x = 22
        y = 7
        n = 15
        Eulerian.precisionCompute(x, y, n)
        print()
