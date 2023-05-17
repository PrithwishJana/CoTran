import math

class GFG:
    @staticmethod
    def _popcnt32(number):
        counter = 0
        while number > 0:
            if math.fmod(number, 2) == 1:
                counter += 1
            number = math.trunc(number / float(2))
        return counter
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maximize(a):
        n = GFG._popcnt32(a)
        res = 0
        for i in range(1, n + 1):
            res = int(res) | (1 << (32 - i))
        return abs(res)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 1
        print(GFG.maximize(a), end = '')
