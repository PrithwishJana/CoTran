import math

class GFG:
    @staticmethod
    def OddDivCount(a, b):
        res = 0
        for i in range(a, b + 1):
            divCount = 0
            for j in range(1, i + 1):
                if math.fmod(i, j) == 0:
                    divCount += 1
            if (math.fmod(divCount, 2)) != 0:
                res += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 1
        b = 10
        print(GFG.OddDivCount(a, b))
