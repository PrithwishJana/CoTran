import math

class GFG:
    M = 20
    dp = [[[[0 for _ in range(2)] for _ in range(M)] for _ in range(M)] for _ in range(M)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def count(pos, firstD, lastD, tight, num):
        if pos == len(num):
            if firstD == lastD:
                return 1
            return 0
        if GFG.dp [pos][firstD][lastD][tight] != - 1:
            return GFG.dp [pos][firstD][lastD][tight]
        ans = 0
        limit = (9 if tight == 1 else num.elementAt(pos))
        for dig in range(0, limit + 1):
            currFirst = firstD
            if pos == 0:
                currFirst = dig
            if currFirst == 0 and dig != 0:
                currFirst = dig
            currTight = tight
            if dig < num.elementAt(pos):
                currTight = 1
            ans += GFG.count(pos + 1, currFirst, dig, currTight, num)
        return GFG.dp [pos][firstD][lastD][tight] = ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(x):
        num = []
        while x > 0:
            num.append(math.fmod(x, 10))
            x = math.trunc(x / float(10))
        num.reverse()
        i = 0
        while i < GFG.M:
            j = 0
            while j < GFG.M:
                k = 0
                while k < GFG.M:
                    for l in range(0, 2):
                        GFG.dp [i][j][k][l] = - 1
                    k += 1
                j += 1
            i += 1
        return GFG.count(0, 0, 0, 0, num)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 2
        R = 60
        print(GFG.solve(R) - GFG.solve(L - 1))
        L = 1
        R = 1000
        print(GFG.solve(R) - GFG.solve(L - 1))
