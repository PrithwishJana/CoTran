class GFG:
    @staticmethod
    def LiesInsieRectangle(a, b, x, y):
        if x - y - b <= 0 and x - y + b >= 0 and x + y - 2 * a + b <= 0 and x + y - b >= 0:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 7
        b = 2
        x = 4
        y = 5
        if GFG.LiesInsieRectangle(a, b, x, y):
            print("Given point lies " + "inside the rectangle")
        else:
            print("Given point does not " + "lie on the rectangle")
