class GFG:
    DP_S = 9
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getNumMonotone(len):
        DP = [[0 for _ in range(GFG.DP_S)] for _ in range(len)]
        for i in range(0, GFG.DP_S):
            DP [0][i] = i + 1
        for i in range(0, len):
            DP [i][0] = 1
        for i in range(1, len):
            for j in range(1, GFG.DP_S):
                DP [i][j] = DP [i - 1][j] + DP [i][j - 1]
        return DP [len - 1][GFG.DP_S - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.getNumMonotone(10))
