import math

class GFG:
    @staticmethod
    def findAandB(N):
        val = N * N - 4.0 * N
        if val < 0:
            print("NO")
            return
        a = (N + math.sqrt(val)) / 2.0
        b = (N - math.sqrt(val)) / 2.0
        print("a = " + str(a))
        print("b = " + str(b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 69.0
        GFG.findAandB(N)
