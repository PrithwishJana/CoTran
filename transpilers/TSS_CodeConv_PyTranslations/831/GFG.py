class GFG:
    @staticmethod
    def centeredHexagonalSeries(n):
        for i in range(1, n + 1):
            print(str(3 * i * (i - 1)) + str(1) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        GFG.centeredHexagonalSeries(n)
