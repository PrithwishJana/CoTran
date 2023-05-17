class GFG:
    maxN = 20
    maxM = 64
    dp = [[0 for _ in range(maxM)] for _ in range(maxN)]
    v = [[False for _ in range(maxM)] for _ in range(maxN)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findLen(arr, i, curr, n, m):
        if i == n:
            if curr == m:
                return 0
            else:
                return - 1
        if GFG.v [i][curr]:
            return GFG.dp [i][curr]
        GFG.v [i][curr] = True
        l = GFG.findLen(arr, i + 1, curr, n, m)
        r = GFG.findLen(arr, i + 1, curr | arr [i], n, m)
        GFG.dp [i][curr] = l
        if r != - 1:
            GFG.dp [i][curr] = max(GFG.dp [i][curr], r + 1)
        return GFG.dp [i][curr]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 7, 2, 3]
        n = len(arr)
        m = 3
        ans = GFG.findLen(arr, 0, 0, n, m)
        if ans == - 1:
            print(0)
        else:
            print(ans)
