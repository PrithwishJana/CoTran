class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def numberOfWays(x):
        if x == 0 or x == 1:
            return 1
        else:
            return GFG.numberOfWays(x - 1) + (x - 1) * GFG.numberOfWays(x - 2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 3
        print(GFG.numberOfWays(x))
