import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if b == 0:
            return a
        return GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
    def noOfSquares(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        ans = dx + dy - GFG.__gcd(dx, dy)
        print(ans)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x1 = 1
        y1 = 1
        x2 = 4
        y2 = 3
        GFG.noOfSquares(x1, y1, x2, y2)
