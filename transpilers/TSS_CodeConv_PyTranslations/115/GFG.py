class GFG:
    @staticmethod
    def line(x0, y0):
        c = int((2 * y0 * x0))
        print("{0:.1f}".format(y0) + "x" + " + " + "{0:.1f}".format(x0) + "y = " + "{0:.1f}".format(c))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x0 = 4
        y0 = 3
        GFG.line(x0, y0)
