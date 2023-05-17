class GFG:
    @staticmethod
    def minRemove(a, b, n, m):
        countA = {}
        countB = {}
        for i in range(0, n):
            if a [i] in countA.keys():
                countA[a [i]] = countA[a [i]] + 1
            else:
                countA[a [i]] = 1
        for i in range(0, m):
            if b [i] in countB.keys():
                countB[b [i]] = countB[b [i]] + 1
            else:
                countB[b [i]] = 1
        res = 0
        s = countA.keys()
        for x in s:
            if x in countB.keys():
                res += min(countB[x], countA[x])
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 2, 3, 4]
        b = [2, 3, 4, 5, 8]
        n = len(a)
        m = len(b)
        print(GFG.minRemove(a, b, n, m))
