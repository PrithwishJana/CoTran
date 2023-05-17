import math

class GFG:
    MAXN = 1000001
    spf = [0 for _ in range(MAXN)]
    hash1 = [0 for _ in range(MAXN)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sieve():
        GFG.spf [1] = 1
        for i in range(2, GFG.MAXN):
            GFG.spf [i] = i
        for i in range(4, GFG.MAXN, 2):
            GFG.spf [i] = 2
        i = 3
        while i * i < GFG.MAXN:
            if GFG.spf [i] == i:
                for j in range(i * i, GFG.MAXN, i):
                    if GFG.spf [j] == j:
                        GFG.spf [j] = i
            i += 1
    @staticmethod
    def getFactorization(x):
        temp = 0
        while x != 1:
            temp = GFG.spf [x]
            if math.fmod(x, temp) == 0:
                GFG.hash1 [GFG.spf [x]] += 1
                x = math.trunc(x / float(GFG.spf [x]))
            while math.fmod(x, temp) == 0:
                x = math.trunc(x / float(temp))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(x):
        temp = 0
        while x != 1:
            temp = GFG.spf [x]
            if math.fmod(x, temp) == 0 and GFG.hash1 [temp] > 1:
                return False
            while math.fmod(x, temp) == 0:
                x = math.trunc(x / float(temp))
        return True
    @staticmethod
    def hasValidNum(arr, n):
        GFG.sieve()
        for i in range(0, n):
            GFG.getFactorization(arr [i])
        for i in range(0, n):
            if GFG.check(arr [i]):
                return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 8, 4, 10, 6, 7]
        n = len(arr)
        if GFG.hasValidNum(arr, n):
            print("Yes")
        else:
            print("No")
