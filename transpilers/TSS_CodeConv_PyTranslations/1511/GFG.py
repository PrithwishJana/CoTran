class GFG:
    @staticmethod
    def highestPowerOf2(n):
        return (n & (~ (n - 1)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 48
        print(GFG.highestPowerOf2(n))
