class GFG:
    @staticmethod
    def FindPoint(x1, y1, x2, y2, x, y):
        if x > x1 and x < x2 and y > y1 and y < y2:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x1 = 0
        y1 = 0
        x2 = 10
        y2 = 8
        x = 1
        y = 5
        if GFG.FindPoint(x1, y1, x2, y2, x, y):
            print("Yes")
        else:
            print("No")
