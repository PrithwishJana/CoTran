import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(ang, n):
        if (ang * n) > (180 * (n - 2)):
            return 0
        elif math.fmod((ang * n), 180) != 0:
            return 0
        ans = 1
        freq = math.trunc((ang * n) / float(180))
        ans = ans * (n - 1 - freq)
        ans = ans * n
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        ang = 90
        n = 4
        print(GFG.solve(ang, n))
