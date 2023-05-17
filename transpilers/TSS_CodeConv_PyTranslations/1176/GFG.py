import math

class GFG:
    @staticmethod
    def calculate_sum(a, N):
        m = math.trunc(N / float(a))
        sum = math.trunc(m * (m + 1) / float(2))
        ans = a * sum
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 7
        N = 49
        print("Sum of multiples of " + str(a) + " up to " + str(N) + " = " + str(GFG.calculate_sum(a, N)))
