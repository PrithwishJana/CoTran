import math

class HocJava:
    @staticmethod
    def main(args):
        sc = java.util.Scanner(System.in)
        n = 0
        mod = 1000000007
        n = sc.nextInt()
        res = 0
        c = [[0 for _ in range(4050)] for _ in range(4050)]
        dp = [0 for _ in range(4050)]
        for i in range(1, n + 1):
            c [i][0] = 1
            for j in range(1, i):
                c [i][j] = math.fmod((c [i - 1][j - 1] + c [i - 1][j]), mod)
            c [i][i] = 1
        dp [0] = 1
        dp [1] = 1
        for i in range(2, n):
            for j in range(0, i):
                dp [i] = math.fmod((dp [i] + dp [j] * c [i - 1][j]), mod)
        for i in range(0, n):
            g = math.fmod(dp [i] * c [n][i], mod)
            res = math.fmod((res + g), mod)
        print(res)
