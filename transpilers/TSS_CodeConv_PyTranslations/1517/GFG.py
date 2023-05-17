class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def smallest(x, y, z):
        c = 0
        while x != 0 and y != 0 and z != 0:
            x -= 1
            y -= 1
            z -= 1
            c += 1
        return c
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 12
        y = 15
        z = 5
        print("Minimum of 3" + " numbers is {0:d}".format(GFG.smallest(x, y, z)), end = '')
