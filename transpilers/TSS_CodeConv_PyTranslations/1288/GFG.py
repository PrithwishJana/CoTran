class GFG:
    @staticmethod
    def toggleBitsFromLToR(n, l, r):
        num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
        return (n ^ num)
    @staticmethod
    def unsetBitsInGivenRange(n, l, r):
        num = (1 << (4 * 8 - 1)) - 1
        num = GFG.toggleBitsFromLToR(num, l, r)
        return (n & num)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 42
        l = 2
        r = 5
        print(GFG.unsetBitsInGivenRange(n, l, r))
