class GFG:
    PI = 3.14159265
    @staticmethod
    def area_leaf(a):
        return (a * a * (GFG.PI / 2 - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 7
        print(GFG.area_leaf(a))
