import math

class GFG:
    v = list  ()
    dp = [[[[0 for _ in range(2)] for _ in range(180)] for _ in range(180)] for _ in range(18)]
    @staticmethod
    def memo(index, evenSum, oddSum, tight):
        if index == len(GFG.v):
            if evenSum > oddSum:
                return 1
            else:
                return 0
        if GFG.dp [index][evenSum][oddSum][tight] != - 1:
            return GFG.dp [index][evenSum][oddSum][tight]
        limit = GFG.v[index] if (tight > 0) else 9
        ans = 0
        for d in range(0, limit + 1):
            currTight = 0
            if d == GFG.v[index]:
                currTight = tight
            if math.fmod(d, 2) != 0:
                ans += GFG.memo(index + 1, evenSum, oddSum + d, currTight)
            else:
                ans += GFG.memo(index + 1, evenSum + d, oddSum, currTight)
        GFG.dp [index][evenSum][oddSum][tight] = ans
        return ans
    @staticmethod
    def CountNum(n):
        GFG.v.clear()
        while n > 0:
            GFG.v.append(math.fmod(n, 10))
            n = math.trunc(n / float(10))
        GFG.v.reverse()
        for i in range(0, 18):
            for j in range(0, 180):
                for k in range(0, 180):
                    for l in range(0, 2):
                        GFG.dp [i][j][k][l] = - 1
        return GFG.memo(0, 0, 0, 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 0
        R = 0
        L = 2
        R = 10
        print(GFG.CountNum(R) - GFG.CountNum(L - 1))
