import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 6
        Even = math.trunc(N / float(2))
        Odd = N - Even
        print(Even * Odd)
