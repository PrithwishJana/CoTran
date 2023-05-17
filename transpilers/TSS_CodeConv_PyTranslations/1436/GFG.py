class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isKthBitSet(n, k):
        if (n >> (k - 1)) == 1:
            return True
        return False
    @staticmethod
    def setKthBit(n, k):
        return ((1 << (k - 1)) | n)
    @staticmethod
    def allBitsAreSet(n):
        if ((n + 1) & n) == 0:
            return True
        return False
    @staticmethod
    def bitsAreInAltOrder(n):
        num = n ^ (n >> 1)
        return GFG.allBitsAreSet(num)
    @staticmethod
    def bitsAreInAltPatrnInGivenRange(n, l, r):
        num = 0
        left_shift = 0
        if GFG.isKthBitSet(n, r):
            num = n
            left_shift = r
        else:
            num = GFG.setKthBit(n, (r + 1))
            left_shift = r + 1
        num = num & ((1 << left_shift) - 1)
        num = num >> (l - 1)
        return GFG.bitsAreInAltOrder(num)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 18
        l = 1
        r = 3
        if GFG.bitsAreInAltPatrnInGivenRange(n, l, r):
            print("Yes")
        else:
            print("No")
