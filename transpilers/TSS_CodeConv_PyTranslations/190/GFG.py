import math

class GFG:
    MOD = 1000000007
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countStrings(N):
        i = 0
        j = 0
        dp = [[0 for _ in range(3)] for _ in range(N + 1)]
        i = 0
        while i < N + 1:
            for j in range(9, 3):
                dp [i][j] = 0
            i += 1
        dp [1][0] = 1
        dp [1][1] = 1
        dp [1][2] = 0
        for i in range(2, N + 1):
            dp [i][0] = math.fmod((dp [i - 1][0] + dp [i - 1][1] + dp [i - 1][2]), GFG.MOD)
            dp [i][1] = math.fmod(dp [i - 1][0], GFG.MOD)
            dp [i][2] = math.fmod(dp [i - 1][1], GFG.MOD)
        ans = math.fmod((dp [N][0] + dp [N][1] + dp [N][2]), GFG.MOD)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        print(GFG.countStrings(N))
