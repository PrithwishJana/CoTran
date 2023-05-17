class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printPattern(i, j, n):
        if j >= n:
            return 0
        if i >= n:
            return 1
        if j == i or j == n - 1 - i:
            if i == n - 1 - j:
                print("/", end = '')
            else:
                print("\\", end = '')
        else:
            print("*", end = '')
        if GFG.printPattern(i, j + 1, n) == 1:
            return 1
        print()
        return GFG.printPattern(i + 1, 0, n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 9
        GFG.printPattern(0, 0, N)
