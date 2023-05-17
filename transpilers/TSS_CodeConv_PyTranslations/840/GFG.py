class GFG:
    @staticmethod
    def Vertices(x, y):
        val = abs(x) + abs(y)
        print(val * (- 1 if x < 0 else 1) + " 0 ", end = '')
        print("0 " + val * (- 1 if y < 0 else 1), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 3
        y = 3
        GFG.Vertices(x, y)
