class GFG:
    @staticmethod
    def bin(n):
        if n > 1:
            GFG.bin(n >> 1)
        print("{0:d}".format(n & 1), end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.bin(131)
        print("\n", end = '')
        GFG.bin(3)
