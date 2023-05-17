class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def max(a, b):
        return a if (a > b) else b
    @staticmethod
    def printknapSack(W, wt, val, n):
        i = 0
        w = 0
        K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            for w in range(0, W + 1):
                if i == 0 or w == 0:
                    K [i][w] = 0
                elif wt [i - 1] <= w:
                    K [i][w] = max(val [i - 1] + K [i - 1][w - wt [i - 1]], K [i - 1][w])
                else:
                    K [i][w] = K [i - 1][w]
        res = K [n][W]
        print(res)
        w = W
        i = n
        while i > 0 and res > 0:
            if res == K [i - 1][w]:
                i -= 1
                continue
            else:
                print(str(wt [i - 1]) + " ", end = '')
                res = res - val [i - 1]
                w = w - wt [i - 1]
            i -= 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 50
        n = len(val)
        GFG.printknapSack(W, wt, val, n)
