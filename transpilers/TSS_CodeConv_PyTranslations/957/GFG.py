import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(n):
        count = 0
        for x in range(1, n):
            for y in range(x + 1, n + 1):
                if math.fmod((y * x), (y + x)) == 0:
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 15
        print(GFG.countPairs(n))
