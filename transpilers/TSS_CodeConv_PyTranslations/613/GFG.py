import math

class GFG:
    @staticmethod
    def summation(n):
        abs_sum = math.trunc(n * (n + 1) / float(2))
        sign = 1 if n + math.fmod(1, 2) == 0 else - 1
        result_sum = sign * abs_sum
        return result_sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 2
        print(GFG.summation(N))
