import math

class GFG:
    MOD = int((1e9 + 7))
    @staticmethod
    def modulo_13(s, n):
        dp = [[0 for _ in range(13)] for _ in range(n + 1)]
        dp [0][0] = 1
        for i in range(0, n):
            for j in range(0, 10):
                nxt = s[i] - '0'
                if s[i] == '?':
                    nxt = j
                for k in range(0, 13):
                    rem = math.fmod((10 * k + nxt), 13)
                    dp [i + 1][rem] += dp [i][k]
                    dp [i + 1][rem] = math.fmod(dp [i + 1][rem], GFG.MOD)
                if s[i] != '?':
                    break
        return int(dp [n][5])
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "?44"
        n = len(s)
        print(GFG.modulo_13(s, n))
