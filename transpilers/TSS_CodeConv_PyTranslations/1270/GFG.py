class GFG:
    @staticmethod
    def isInside(circle_x, circle_y, rad, x, y):
        if (x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        x = 1
        y = 1
        circle_x = 0
        circle_y = 1
        rad = 2
        if GFG.isInside(circle_x, circle_y, rad, x, y):
            print("Inside", end = '')
        else:
            print("Outside", end = '')
