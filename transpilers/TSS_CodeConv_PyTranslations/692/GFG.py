import math

class GFG:
    @staticmethod
    def arrange(N):
        if N == 1:
            print("1")
            return
        if N == 2 or N == 3:
            print("-1")
            return
        even = - 1
        odd = - 1
        if math.fmod(N, 2) == 0:
            even = N
            odd = N - 1
        else:
            odd = N
            even = N - 1
        while odd >= 1:
            print(odd, end = '')
            print(" ", end = '')
            odd = odd - 2
        while even >= 2:
            print(even, end = '')
            print(" ", end = '')
            even = even - 2
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 5
        GFG.arrange(N)
