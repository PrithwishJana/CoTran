import math

class Smooth:
    sc = Scanner(System.in)
    memo = [[0 for _ in range(257)] for _ in range(100)]
    @staticmethod
    def main(args):
        T = Smooth.sc.nextInt()
        for i in range(1, T + 1):
            print("Case #" + str(i) + ": ", end = '')
            Smooth.solveCase()
    SPC = 256
    @staticmethod
    def solveCase():
        Smooth.del_ = Smooth.sc.nextInt()
        Smooth.ins = Smooth.sc.nextInt()
        Smooth.maxDist = Smooth.sc.nextInt()
        Smooth.n = Smooth.sc.nextInt()
        Smooth.arr = [0 for _ in range(Smooth.n)]
        i = 0
        while i < Smooth.n:
            Smooth.arr [i] = Smooth.sc.nextInt()
            i += 1
        for arr in Smooth.memo:
            Arrays.fill(arr, - 1)
        print(Smooth.solve(0, Smooth.SPC))
    del_ = 0
    ins = 0
    maxDist = 0
    n = 0
    arr = None
    @staticmethod
    def solve(index, prev):
        if index >= Smooth.n:
            return 0
        if Smooth.memo [index][prev] == - 1:
            res = Smooth.del_ + Smooth.solve(index + 1, prev)
            for val in range(0, Smooth.SPC):
                res = min(res, abs(Smooth.arr [index] - val) + Smooth.insCost(val, prev) + Smooth.solve(index + 1, val))
            Smooth.memo [index][prev] = res
        return Smooth.memo [index][prev]
    @staticmethod
    def insCost(cur, prev):
        if prev == Smooth.SPC or cur == prev:
            return 0
        if Smooth.maxDist == 0:
            return 100000000
        return Smooth.ins * (math.trunc((abs(cur - prev) + Smooth.maxDist - 1) / float(Smooth.maxDist)) - 1)
