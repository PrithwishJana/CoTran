import math

class GFG:
    @staticmethod
    def trailing_zeros(N):
        count_of_two = 0
        count_of_five = 0
        for i in range(1, N + 1):
            val = i
            while math.fmod(val, 2) == 0 and val > 0:
                val = math.trunc(val / float(2))
                count_of_two += i
            while math.fmod(val, 5) == 0 and val > 0:
                val = math.trunc(val / float(5))
                count_of_five += i
        ans = min(count_of_two, count_of_five)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 12
        print(GFG.trailing_zeros(N))
