class GFG:
    @staticmethod
    def Subtract(a, b):
        c = 0
        c = a + (~ b + 1)
        return c
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 2
        b = 3
        print(GFG.Subtract(a, b))
        a = 9
        b = 7
        print(GFG.Subtract(a, b))
