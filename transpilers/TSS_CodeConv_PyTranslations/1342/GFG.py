class GFG:
    @staticmethod
    def getModulo(n, d):
        return (n & (d - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        d = 4
        print(str(n) + " moduo " + str(d) + " is " + str(GFG.getModulo(n, d)))
