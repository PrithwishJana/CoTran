class GFG:
    @staticmethod
    def findThirdDigit(n):
        if n < 3:
            return 0
        return 1 if (n & 1) > 0 else 6
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 7
        print(GFG.findThirdDigit(n))
