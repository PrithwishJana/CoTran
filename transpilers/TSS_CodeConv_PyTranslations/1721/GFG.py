import math

class GFG:
    @staticmethod
    def steps(cur, x, n):
        if x == 0:
            return Integer.MAX_VALUE
        if x > 0:
            return abs(math.trunc((n - cur) / float(x)))
        else:
            return abs(math.trunc((cur - 1) / float(x)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSteps(curx, cury, n, m, moves):
        count = 0
        k = len(moves)
        for i in range(0, k):
            x = moves [i][0]
            y = moves [i][1]
            stepct = min(GFG.steps(curx, x, n), GFG.steps(cury, y, m))
            count += stepct
            curx += stepct * x
            cury += stepct * y
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        m = 5
        x = 1
        y = 1
        moves = [[ 1, 1 ], [ 1, 1 ], [ 0, - 2 ]]
        print(GFG.countSteps(x, y, n, m, moves), end = '')
