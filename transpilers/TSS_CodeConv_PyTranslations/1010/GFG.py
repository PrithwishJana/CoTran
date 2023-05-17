class GFG:
    l = [[0 for _ in range(1001)] for _ in range(1001)]
    @staticmethod
    def initialize():
        GFG.l [0][0] = 1
        for i in range(1, 1001):
            GFG.l [i][0] = 1
            j = 1
            while j < i + 1:
                GFG.l [i][j] = (GFG.l [i - 1][j - 1] + GFG.l [i - 1][j])
                j += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nCr(n, r):
        return GFG.l [n][r]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.initialize()
        n = 8
        r = 3
        print(GFG.nCr(n, r))
