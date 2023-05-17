class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sum(k, n):
        sum = int((k ** (n + 1) - (k - 1) ** (n + 1)))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        K = 3
        print(GFG.sum(K, n), end = '')
