import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(n, m):
        if math.fmod(m, n) == 0:
            print("YES", end = '')
        else:
            print("NO", end = '')
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        m = 10
        GFG.check(n, m)
