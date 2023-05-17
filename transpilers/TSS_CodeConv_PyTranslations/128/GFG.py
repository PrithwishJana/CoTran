import math

class GFG:
    @staticmethod
    def isSpiltPossible(n, a):
        sum = 0
        c1 = 0
        for i in range(0, n):
            sum += a [i]
            if a [i] == 1:
                c1 += 1
        if math.fmod(sum, 2) != 0:
            return False
        if math.fmod((math.trunc(sum / float(2))), 2) == 0:
            return True
        if c1 > 0:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        a = [1, 1, 2]
        if GFG.isSpiltPossible(n, a):
            print("YES")
        else:
            print("NO")
