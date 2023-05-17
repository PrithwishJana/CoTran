import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def check(n, m):
        if n == 2 or m == 2 or math.fmod(n, m) == 0:
            print("Yes")
        else:
            print("No")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        m = 3
        n = 9
        GFG.check(n, m)
