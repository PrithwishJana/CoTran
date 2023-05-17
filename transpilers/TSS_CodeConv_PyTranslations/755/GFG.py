class GFG:
    @staticmethod
    def index(i):
        return 1 + (i >> 31) - (- i >> 31)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(n):
        s = ["negative", "zero", "positive"]
        val = GFG.index(n)
        print(str(n) + " is " + s [val])
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        GFG.check(30)
        GFG.check(- 20)
        GFG.check(0)
