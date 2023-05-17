class GFG:
    @staticmethod
    def f(x, y):
        v = y - 2 * x * x + 1
        return v
    @staticmethod
    def predict(x, y, h):
        y1p = y + h * GFG.f(x, y)
        return y1p
    @staticmethod
    def correct(x, y, x1, y1, h):
        e = 0.00001
        y1c = y1
        while abs(y1c - y1) > e:
            y1 = y1c
            y1c = y + 0.5 * h * (GFG.f(x, y) + GFG.f(x1, y1))
        return y1c
    @staticmethod
    def printFinalValues(x, xn, y, h):
        while x < xn:
            x1 = x + h
            y1p = GFG.predict(x, y, h)
            y1c = GFG.correct(x, y, x1, y1p, h)
            x = x1
            y = y1c
        print("The final value of y at x = " + str(int(x)) + " is : " + "{0:.4f}".format(y))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 0
        y = 0.5
        xn = 1
        h = 0.2
        GFG.printFinalValues(x, xn, y, h)
