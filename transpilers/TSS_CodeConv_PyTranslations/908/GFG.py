class GFG:
    @staticmethod
    def findPoint(x1, y1, x2, y2):
        print("(" + str(int((2 * x2 - x1))) + "," + str(int((2 * y2 - y1))) + " )")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x1 = 0
        y1 = 0
        x2 = 1
        y2 = 1
        GFG.findPoint(x1, y1, x2, y2)
