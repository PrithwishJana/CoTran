class GFG:
    @staticmethod
    def min(x, y, z):
        if x < y:
            return x if (x < z) else z
        else:
            return y if (y < z) else z
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def minCost(cost, m, n):
        if n < 0 or m < 0:
            return Integer.MAX_VALUE
        elif m == 0 and n == 0:
            return cost [m][n]
        else:
            return cost [m][n] + GFG.min(GFG.minCost(cost, m - 1, n - 1), GFG.minCost(cost, m - 1, n), GFG.minCost(cost, m, n - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        cost = [[ 1, 2, 3 ], [ 4, 8, 2 ], [ 1, 5, 3 ]]
        print(GFG.minCost(cost, 2, 2), end = '')
