class GFG:
    @staticmethod
    def hexDiagonal(a):
        if a < 0:
            return - 1
        d = float(1.73) * a
        return d
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 9
        print(GFG.hexDiagonal(a))
