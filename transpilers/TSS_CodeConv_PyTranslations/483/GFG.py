class GFG:
    @staticmethod
    def doublefactorial(n):
        if n == 0 or n == 1:
            return 1
        return n * GFG.doublefactorial(n - 2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print("Double factorial" + " is " + str(GFG.doublefactorial(5)))
