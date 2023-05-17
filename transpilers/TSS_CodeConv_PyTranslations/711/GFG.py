class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n, m):
        count = [0 for _ in range(n + 1)]
        count [0] = 0
        i = 0
        for i in range(1, n + 1):
            if i > m:
                count [i] = count [i - 1] + count [i - m]
            elif i < m:
                count [i] = 1
            else:
                count [i] = 2
        return count [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        m = 4
        print("Number of ways = " + str(GFG.countWays(n, m)))
