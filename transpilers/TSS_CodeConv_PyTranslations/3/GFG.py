import math

class GFG:
    @staticmethod
    def count9s(number):
        n = len(number)
        d = [0 for _ in range(9)]
        d [0] = 1
        result = 0
        mod_sum = 0
        continuous_zero = 0
        for i in range(0, n):
            if (number [i] - '0') == 0:
                continuous_zero += 1
            else:
                continuous_zero = 0
            mod_sum += (number [i] - '0')
            mod_sum = math.fmod(mod_sum, 9)
            result += d [mod_sum]
            d [mod_sum] += 1
            result -= continuous_zero
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.count9s("01809" .toCharArray()))
        print(GFG.count9s("1809" .toCharArray()))
        print(GFG.count9s("4189" .toCharArray()))
