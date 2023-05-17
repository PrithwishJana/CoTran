import math

class GFG:
    @staticmethod
    def pentagon_pyramidal(n):
        sum = 0
        for i in range(1, n + 1):
            p = math.trunc((3 * i * i - i) / float(2))
            sum = sum + p
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print(GFG.pentagon_pyramidal(n))
