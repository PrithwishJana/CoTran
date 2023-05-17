class GFG:
    @staticmethod
    def Area(a):
        if a < 0:
            return - 1
        h = float(1.268) * a
        A = float((0.70477 * h ** 2))
        return A
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 5
        print(GFG.Area(a))
