import math

class GFG:
    N = 6
    m = 6
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxSum(arr):
        dp = [[0 for _ in range(3)] for _ in range(GFG.N + 1)]
        i = 0
        while i < GFG.N:
            m1 = 0
            m2 = 0
            m3 = 0
            j = 0
            while j < GFG.m:
                if (math.trunc(j / float(math.trunc(GFG.m / float(3))))) == 0:
                    m1 = max(m1, arr [i][j])
                elif (math.trunc(j / float(math.trunc(GFG.m / float(3))))) == 1:
                    m2 = max(m2, arr [i][j])
                elif (math.trunc(j / float(math.trunc(GFG.m / float(3))))) == 2:
                    m3 = max(m3, arr [i][j])
                j += 1
            dp [i + 1][0] = max(dp [i][1], dp [i][2]) + m1
            dp [i + 1][1] = max(dp [i][0], dp [i][2]) + m2
            dp [i + 1][2] = max(dp [i][1], dp [i][0]) + m3
            i += 1
        print(str(max(max(dp [GFG.N][0], dp [GFG.N][1]), dp [GFG.N][2])) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [[ 1, 3, 5, 2, 4, 6 ], [ 6, 4, 5, 1, 3, 2 ], [ 1, 3, 5, 2, 4, 6 ], [ 6, 4, 5, 1, 3, 2 ], [ 6, 4, 5, 1, 3, 2 ], [ 1, 3, 5, 2, 4, 6 ]]
        GFG.maxSum(arr)
