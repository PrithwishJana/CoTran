class solution:
    @staticmethod
    def circle_equation(x1, y1, r):
        a = - 2 * x1
        b = - 2 * y1
        c = (r * r) - (x1 * x1) - (y1 * y1)
        print("x^2 + (" + str(a) + " x) + ", end = '')
        print("y^2 + (" + str(b) + " y) = ", end = '')
        print(str(c) + ".")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arr):
        x1 = 2
        y1 = - 3
        r = 8
        solution.circle_equation(x1, y1, r)
