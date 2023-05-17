import math

class solution:
    @staticmethod
    def Squares(n, m, a):
        return (math.trunc((m + a - 1) / float(a))) * (math.trunc((n + a - 1) / float(a)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arr):
        n = 6
        m = 6
        a = 4
        print(solution.Squares(n, m, a))
