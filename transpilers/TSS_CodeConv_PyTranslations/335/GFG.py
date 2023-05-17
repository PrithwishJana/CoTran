import math

class GFG:
    @staticmethod
    def modInverse(a, m):
        a = math.fmod(a, m)
        for x in range(1, m):
            if math.fmod((a * x), m) == 1:
                return x
        return 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 3
        m = 11
        print(GFG.modInverse(a, m))
