import math

class Solution:
    M = 20
    dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(M)] for _ in range(M)]
    d = 0
    K = 0
    @staticmethod
    def count(pos, cnt, tight, nonz, num):
        if pos == len(num):
            if cnt == Solution.K:
                return 1
            return 0
        if Solution.dp [pos][cnt][tight][nonz] != - 1:
            return Solution.dp [pos][cnt][tight][nonz]
        ans = 0
        limit = (9 if (tight != 0) else num[pos])
        for dig in range(0, limit + 1):
            currCnt = cnt
            if dig == Solution.d:
                if Solution.d != 0 or (Solution.d == 0 and nonz != 0):
                    currCnt += 1
            currTight = tight
            if dig < num[pos]:
                currTight = 1
            ans += Solution.count(pos + 1, currCnt, currTight, (1 if dig != 0 else 0), num)
        return Solution.dp [pos][cnt][tight][nonz] = ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(x):
        num = list  ()
        while x != 0:
            num.append(math.fmod(x, 10))
            x = math.trunc(x / float(10))
        num.reverse()
        for i in range(0, Solution.M):
            for j in range(0, Solution.M):
                for k in range(0, 2):
                    for l in range(0, 2):
                        Solution.dp [i][j][k][l] = - 1
        return Solution.count(0, 0, 0, 0, num)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 11
        R = 100
        Solution.d = 2
        Solution.K = 1
        print(Solution.solve(R) - Solution.solve(L - 1), end = '')
