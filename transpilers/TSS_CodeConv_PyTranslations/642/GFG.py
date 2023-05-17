class GFG:
    @staticmethod
    def multiplyWith3Point5(x):
        return (x << 1) + x + (x >> 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 4
        print(GFG.multiplyWith3Point5(x))
