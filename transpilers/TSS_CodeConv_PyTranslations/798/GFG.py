class GFG:
    @staticmethod
    def circlearea(a, b):
        if a < 0 or b < 0:
            return - 1
        A = float(((3.14 * a ** 2 * b ** 2) / (4 * (a ** 2 + b ** 2))))
        return A
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 8
        b = 10
        print(GFG.circlearea(a, b))
