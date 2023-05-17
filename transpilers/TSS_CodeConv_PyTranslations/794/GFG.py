import math

class GFG:
    MOD = 1000000007
    @staticmethod
    def modFact(n, m):
        result = 1
        for i in range(1, m + 1):
            result = math.fmod((result * i), GFG.MOD)
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        m = 2
        print(GFG.modFact(n, m))
