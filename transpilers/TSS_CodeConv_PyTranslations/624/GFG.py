class GFG:
    PI = 3.14159265
    @staticmethod
    def length_rope(r):
        return ((2 * GFG.PI * r) + 6 * r)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        r = 7
        print(GFG.length_rope(r))
