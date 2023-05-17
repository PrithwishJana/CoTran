class GFG:
    dp = [[0 for _ in range(8101)] for _ in range(901)]
    @staticmethod
    def minimumNumberOfDigits(a, b):
        if a > b or a < 0 or b < 0 or a > 900 or b > 8100:
            return - 1
        if a == 0 and b == 0:
            return 0
        if GFG.dp [a][b] != - 1:
            return GFG.dp [a][b]
        ans = 101
        for i in range(9, 0, -1):
            k = GFG.minimumNumberOfDigits(a - i, b - (i * i))
            if k != - 1:
                ans = min(ans, k + 1)
        return GFG.dp [a][b] = ans
    @staticmethod
    def printSmallestNumber(a, b):
        for row in GFG.dp:
            Arrays.fill(row, - 1)
        GFG.dp [0][0] = 0
        k = GFG.minimumNumberOfDigits(a, b)
        if k == - 1 or k > 100:
            print("-1")
        else:
            while a > 0 and b > 0:
                for i in range(1, 10):
                    if a >= i and b >= i * i and 1 + GFG.dp [a - i][b - i * i] == GFG.dp [a][b]:
                        print(i, end = '')
                        a -= i
                        b -= i * i
                        break
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 18
        b = 162
        GFG.printSmallestNumber(a, b)
