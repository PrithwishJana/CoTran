import math

class GFG:
    @staticmethod
    def findNumberOfEvenCells(n, q, size):
        row = [0 for _ in range(n)]
        col = [0 for _ in range(n)]
        for i in range(0, size):
            x = q [i][0]
            y = q [i][1]
            row [x - 1] += 1
            col [y - 1] += 1
        r1 = 0
        r2 = 0
        c1 = 0
        c2 = 0
        for i in range(0, n):
            if math.fmod(row [i], 2) == 0:
                r1 += 1
            if math.fmod(row [i], 2) == 1:
                r2 += 1
            if math.fmod(col [i], 2) == 0:
                c1 += 1
            if math.fmod(col [i], 2) == 1:
                c2 += 1
        count = r1 * c1 + r2 * c2
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        q = [[ 1, 1 ], [ 1, 2 ], [ 2, 1 ]]
        size = len(q)
        print(GFG.findNumberOfEvenCells(n, q, size))
