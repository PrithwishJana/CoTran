import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(d1, d2, d3):
        maxx = max(d1, max(d2, d3))
        sum = (d1 + d2 + d3)
        if 2 * maxx > sum or math.fmod(sum, 2) == 1:
            print("-1", end = '')
            return
        x1 = 0
        y1 = 0
        x2 = d1
        y2 = 0
        x3 = math.trunc((d1 + d2 - d3) / float(2))
        y3 = math.trunc((d2 + d3 - d1) / float(2))
        print("(" + str(x1) + ", " + str(y1) + "), (" + str(x2) + ", " + str(y2) + ") and (" + str(x3) + ", " + str(y3) + ")", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        d1 = 3
        d2 = 4
        d3 = 5
        GFG.solve(d1, d2, d3)
