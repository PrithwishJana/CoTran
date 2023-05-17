import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSetBits(n):
        cnt = 0
        setBits = [0 for _ in range(n + 1)]
        setBits [0] = 0
        setBits [1] = 1
        for i in range(2, n + 1):
            if math.fmod(i, 2) == 0:
                setBits [i] = setBits [math.trunc(i / float(2))]
            else:
                setBits [i] = setBits [i - 1] + 1
        for i in range(0, n + 1):
            cnt = cnt + setBits [i]
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        print(GFG.countSetBits(n))
