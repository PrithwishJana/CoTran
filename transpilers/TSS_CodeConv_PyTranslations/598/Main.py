class geeks:
    @staticmethod
    def firstSetBit(n):
        x = n & (n - 1)
        return (n ^ x)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12
        print(geeks.firstSetBit(n))
