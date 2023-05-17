import math

class GFG:
    @staticmethod
    def func(x):
        return (1 / (1 + x * x))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculate(lower_limit, upper_limit, interval_limit):
        value = 0
        interval_size = (upper_limit - lower_limit) / interval_limit
        sum = GFG.func(lower_limit) + GFG.func(upper_limit)
        for i in range(1, interval_limit):
            if math.fmod(i, 3) == 0:
                sum = sum + 2 * GFG.func(lower_limit + i * interval_size)
            else:
                sum = sum + 3 * GFG.func(lower_limit + i * interval_size)
        return (3 * interval_size / 8) * sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        interval_limit = 10
        lower_limit = 1
        upper_limit = 10
        integral_res = GFG.calculate(lower_limit, upper_limit, interval_limit)
        print("{0:.4f}".format(integral_res))
