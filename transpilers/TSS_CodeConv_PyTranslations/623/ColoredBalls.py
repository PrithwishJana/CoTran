import math

class ColoredBalls:
    mod = 1000000007
    MAXN = 1010
    @staticmethod
    def main(args):
        in_ = Scanner(System.in)
        out = PrintWriter(System.out, True)
        comb = [[0 for _ in range(ColoredBalls.MAXN)] for _ in range(ColoredBalls.MAXN)]
        comb [0][0] = 1
        i = 1
        while i < ColoredBalls.MAXN:
            comb [i][0] = 1
            for j in range(1, i + 1):
                comb [i][j] = math.fmod((comb [i - 1][j] + comb [i - 1][j - 1]), ColoredBalls.mod)
            i += 1
        K = in_.nextInt()
        color = [0 for _ in range(K)]
        for i in range(0, K):
            color [i] = in_.nextInt()
        res = 1
        total = 0
        for i in range(0, K):
            res = math.fmod((res * comb [total + color [i] - 1][color [i] - 1]), ColoredBalls.mod)
            total += color [i]
        out.println(res)
        out.close()
        System.exit(0)
