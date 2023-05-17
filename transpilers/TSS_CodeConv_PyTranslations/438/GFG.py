class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minimumCost(cost, n):
        dp1 = 0
        dp2 = 0
        for i in range(0, n):
            dp0 = cost [i] + min(dp1, dp2)
            dp2 = dp1
            dp1 = dp0
        return min(dp1, dp2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 5, 3, 1, 7, 3, 4]
        n = len(a)
        print(GFG.minimumCost(a, n), end = '')
