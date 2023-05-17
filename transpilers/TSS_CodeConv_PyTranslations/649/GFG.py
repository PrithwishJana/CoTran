class GFG:
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sum(self, n):
        if n < 2:
            return 1
        else:
            return 1 / n + (self.sum(n - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        g = GFG()
        print("{0:.3f}".format(GFG.sum(8)))
        print("{0:.3f}".format(GFG.sum(10)), end = '')
