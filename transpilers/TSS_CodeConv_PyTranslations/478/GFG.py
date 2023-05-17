class GFG:
    class Query:
        def __init__(self, l, r, n):
            #instance fields found by Java to Python Converter:
            self.l = 0
            self.r = 0
            self.n = 0

            self.l = l
            self.r = r
            self.n = n
    @staticmethod
    def printSmallest(s, q):
        N = len(s)
        H = [[0 for _ in range(26)] for _ in range(N + 1)]
        for i in range(1, N + 1):
            H [i][s[i - 1] - 'a'] += 1
            for j in range(0, 26):
                H [i][j] += H [i - 1][j]
        m = len(q)
        for j in range(0, m):
            l = q [j].l
            r = q [j].r
            n = q [j].n
            sum = 0
            for i in range(0, 26):
                sum += H [r][i] - H [l - 1][i]
                if sum >= n:
                    print(chr(('a' + i)))
                    break
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "afbccdeb"
        q = [Query(2, 4, 1), Query(1, 6, 4), Query(1, 8, 7)]
        GFG.printSmallest(s, q)
