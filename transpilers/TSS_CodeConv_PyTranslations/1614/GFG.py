class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sum(n):
        i = 0
        s = 0.0
        for i in range(1, n + 1):
            s = s + 1 / i
        return s
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print("Sum is {0:f}".format(GFG.sum(n)), end = '')
