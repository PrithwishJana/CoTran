class GFG:
    @staticmethod
    def nonDecNums(n):
        a = [[0 for _ in range(10)] for _ in range(n + 1)]
        for i in range(0, 10):
            a [0][i] = 1
        for i in range(1, n + 1):
            a [i][9] = 1
        for i in range(1, n + 1):
            for j in range(8, -1, -1):
                a [i][j] = a [i - 1][j] + a [i][j + 1]
        return a [n][0]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        print("Non-decreasing digits = " + str(GFG.nonDecNums(n)))
