class GFG:
    @staticmethod
    def triangular_series(n):
        i = 0
        j = 1
        k = 1
        for i in range(1, n + 1):
            print("{0:d} ".format(k), end = '')
            j = j + 1
            k = k + j
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        GFG.triangular_series(n)
