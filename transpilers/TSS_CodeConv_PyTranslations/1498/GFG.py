class GFG:
    @staticmethod
    def grayCode(n):
        return n ^ (n >> 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        print(GFG.grayCode(n))
