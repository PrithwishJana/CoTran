class GFG:
    @staticmethod
    def powerOfTwo(n):
        return ((n & n - 1) == 0)
    @staticmethod
    def onlyFirstAndLastAreSet(n):
        if n == 1:
            return True
        return GFG.powerOfTwo(n - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = Integer.parseUnsignedInt("9")
        if GFG.onlyFirstAndLastAreSet(n):
            print("Yes")
        else:
            print("No")
