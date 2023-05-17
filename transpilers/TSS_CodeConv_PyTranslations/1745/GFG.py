import math

class GFG:
    @staticmethod
    def countNonEmptySubstr(str):
        n = len(str)
        return math.trunc(n * (n + 1) / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "abcde"
        print(GFG.countNonEmptySubstr(s))
