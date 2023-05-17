class GFG:
    @staticmethod
    def findY(x):
        if x > 2:
            return x - 2
        return x + 2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 5
        print(GFG.findY(x))
