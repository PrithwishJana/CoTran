import math

class GFG:
    MOD = 1000000007
    @staticmethod
    def digitNumber(n):
        if n == 0:
            return 1
        if n == 1:
            return 9
        if math.fmod(n, 2) != 0:
            temp = math.fmod(GFG.digitNumber(math.trunc((n - 1) / float(2))), GFG.MOD)
            return math.fmod((math.fmod(9 * (temp * temp), GFG.MOD)), GFG.MOD)
        else:
            temp = math.fmod(GFG.digitNumber(math.trunc(n / float(2))), GFG.MOD)
            return math.fmod((temp * temp), GFG.MOD)
    @staticmethod
    def countExcluding(n, d):
        if d == 0:
            return math.fmod((9 * GFG.digitNumber(n - 1)), GFG.MOD)
        else:
            return math.fmod((8 * GFG.digitNumber(n - 1)), GFG.MOD)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        d = 9
        n = 3
        print(GFG.countExcluding(n, d))
