class GFG:
    @staticmethod
    def mul_table(N, i):
        if i > 10:
            return
        print(str(N) + " * " + str(i) + " = " + str(N * i))
        GFG.mul_table(N, i + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 8
        GFG.mul_table(N, 1)
