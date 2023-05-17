class solution:
    @staticmethod
    def foot(a, b, c, d, x1, y1, z1):
        k = (- a * x1 - b * y1 - c * z1 - d) / float((a * a + b * b + c * c))
        x2 = a * k + x1
        y2 = b * k + y1
        z2 = c * k + z1
        print("x2 = " + "{0:.1f}".format(x2), end = '')
        print(" y2 = " + "{0:.1f}".format(y2), end = '')
        print(" z2 = " + "{0:.1f}".format(z2), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arr):
        a = 1
        b = - 2
        c = 0
        d = 0
        x1 = - 1
        y1 = 3
        z1 = 4
        solution.foot(a, b, c, d, x1, y1, z1)
