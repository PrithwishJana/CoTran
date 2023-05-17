class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxPrimefactorNum(N):
        if N < 2:
            return 0
        arr = [False for _ in range(N + 1)]
        prod = 1
        res = 0
        p = 2
        while p * p <= N:
            if arr [p] == False:
                for i in range(p * 2, N + 1, p):
                    arr [i] = True
                prod *= p
                if prod > N:
                    return res
                res += 1
            p += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 500
        print(GFG.maxPrimefactorNum(N))
