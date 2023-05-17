class GFG:
    @staticmethod
    def MinimumValue(x, y):
        if x > y:
            temp = x
            x = y
            y = temp
        a = 1
        b = x - 1
        c = y - b
        print(str(a) + " " + str(b) + " " + str(c), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 123
        y = 13
        GFG.MinimumValue(x, y)
