class GFG:
    @staticmethod
    def countUnsetBits(n):
        x = n
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        return Integer.bitCount(x ^ n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 17
        print(GFG.countUnsetBits(n))
