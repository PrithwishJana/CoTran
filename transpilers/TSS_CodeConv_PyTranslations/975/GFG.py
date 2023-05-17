import math

class GFG:
    N = 101
    MOD = int(1e)9 + 7
    exactsum = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    exactnum = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getSum(x, y, z):
        ans = 0
        GFG.exactnum [0][0][0] = 1
        for i in range(0, x + 1):
            for j in range(0, y + 1):
                for k in range(0, z + 1):
                    if i > 0:
                        GFG.exactsum [i][j][k] += math.fmod((GFG.exactsum [i - 1][j][k] * 10 + 4 * GFG.exactnum [i - 1][j][k]), GFG.MOD)
                        GFG.exactnum [i][j][k] += math.fmod(GFG.exactnum [i - 1][j][k], GFG.MOD)
                    if j > 0:
                        GFG.exactsum [i][j][k] += math.fmod((GFG.exactsum [i][j - 1][k] * 10 + 5 * GFG.exactnum [i][j - 1][k]), GFG.MOD)
                        GFG.exactnum [i][j][k] += math.fmod(GFG.exactnum [i][j - 1][k], GFG.MOD)
                    if k > 0:
                        GFG.exactsum [i][j][k] += math.fmod((GFG.exactsum [i][j][k - 1] * 10 + 6 * GFG.exactnum [i][j][k - 1]), GFG.MOD)
                        GFG.exactnum [i][j][k] += math.fmod(GFG.exactnum [i][j][k - 1], GFG.MOD)
                    ans += math.fmod(GFG.exactsum [i][j][k], GFG.MOD)
                    ans = math.fmod(ans, GFG.MOD)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 1
        y = 1
        z = 1
        print(math.fmod(GFG.getSum(x, y, z), GFG.MOD))
