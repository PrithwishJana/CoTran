class GFG:
    dp = [[[0 for _ in range(5)] for _ in range(5001)] for _ in range(5001)]
    @staticmethod
    def countWaysUtil(n, parts, nextPart):
        if parts == 0 and n == 0:
            return 1
        if n <= 0 or parts <= 0:
            return 0
        if GFG.dp [n][nextPart][parts] != - 1:
            return GFG.dp [n][nextPart][parts]
        ans = 0
        for i in range(nextPart, n + 1):
            ans += GFG.countWaysUtil(n - i, parts - 1, i)
        return (GFG.dp [n][nextPart][parts] := ans)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n):
        for i in range(0, 5001):
            for j in range(0, 5001):
                for l in range(0, 5):
                    GFG.dp [i][j][l] = - 1
        return GFG.countWaysUtil(n, 4, 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 8
        print(GFG.countWays(n))
