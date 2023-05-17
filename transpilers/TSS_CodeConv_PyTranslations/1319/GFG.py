import math

class GFG:
    @staticmethod
    def get(x, y, z):
        if x > z:
            return - 1
        val = z - x
        div = math.trunc((z - x) / float(y))
        ans = div * y + x
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 1
        y = 5
        z = 8
        print(GFG.get(x, y, z) + "\n", end = '')
