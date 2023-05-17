class GFG:
    @staticmethod
    def CountSetBits(n):
        if n == 0:
            return 0
        if (n & 1) == 1:
            return 1 + GFG.CountSetBits(n >> 1)
        else:
            return GFG.CountSetBits(n >> 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 21
        print(GFG.CountSetBits(n))
