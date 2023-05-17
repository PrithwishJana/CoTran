import math

class GFG:
    @staticmethod
    def centered_heptagonal_num(n):
        return math.trunc((7 * n * n - 7 * n + 2) / float(2))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print(str(n) + "th Centered " + "heptagonal number : " + str(GFG.centered_heptagonal_num(n)))
