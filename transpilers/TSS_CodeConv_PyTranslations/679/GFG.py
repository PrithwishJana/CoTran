class GFG:
    @staticmethod
    def FindPoints(x1, y1, x2, y2, x3, y3, x4, y4):
        x5 = max(x1, x3)
        y5 = max(y1, y3)
        x6 = min(x2, x4)
        y6 = min(y2, y4)
        if x5 > x6 or y5 > y6:
            print("No intersection")
            return
        print("(" + str(x5) + ", " + str(y5) + ") ", end = '')
        print("(" + str(x6) + ", " + str(y6) + ") ", end = '')
        x7 = x5
        y7 = y6
        print("(" + str(x7) + ", " + str(y7) + ") ", end = '')
        x8 = x6
        y8 = y5
        print("(" + str(x8) + ", " + str(y8) + ") ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x1 = 0
        y1 = 0
        x2 = 10
        y2 = 8
        x3 = 2
        y3 = 3
        x4 = 7
        y4 = 9
        GFG.FindPoints(x1, y1, x2, y2, x3, y3, x4, y4)
