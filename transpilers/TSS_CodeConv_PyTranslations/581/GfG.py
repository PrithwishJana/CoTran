class GfG:
    @staticmethod
    def toggleLastMBits(n, m):
        num = (1 << m) - 1
        return (n ^ num)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(argc):
        n = 107
        m = 4
        n = GfG.toggleLastMBits(n, m)
        print(n)
