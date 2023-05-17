class GFG:
    @staticmethod
    def Circular(n):
        Result = 1
        while n > 0:
            Result = Result * n
            n -= 1
        return Result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print(GFG.Circular(n - 1))
