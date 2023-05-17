class GFG:
    @staticmethod
    def rectanglearea(a, b):
        if a < 0 or b < 0:
            return - 1
        return 2 * a * b
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 10
        b = 8
        print(GFG.rectanglearea(a, b))
