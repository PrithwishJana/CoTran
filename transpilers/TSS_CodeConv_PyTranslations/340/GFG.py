class GFG:
    @staticmethod
    def bitsAreInAltPatrnInGivenTRange(n, l, r):
        num = 0
        prev = 0
        curr = 0
        num = n >> (l - 1)
        prev = num & 1
        num = num >> 1
        i = 1
        while i <= (r - l):
            curr = num & 1
            if curr == prev:
                return False
            prev = curr
            num = num >> 1
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 18
        l = 1
        r = 3
        if GFG.bitsAreInAltPatrnInGivenTRange(n, l, r):
            print("Yes")
        else:
            print("No")
