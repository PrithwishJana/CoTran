import math

class GFG:
    @staticmethod
    def evaluate(n):
        if n == 1 or n == 2:
            print("No Pythagoras " + "Triplet exists")
        elif math.fmod(n, 2) == 0:
            var = math.trunc(1 * n * n / float(4))
            print("Pythagoras Triplets " + "exist i.e. ", end = '')
            print(str(n) + " ", end = '')
            print(var str(- 1) + " ", end = '')
            print(str(var) + str(1) + " ")
        elif math.fmod(n, 2) != 0:
            var = 1 * n * n + 1
            print("Pythagoras Triplets " + "exist i.e. ", end = '')
            print(str(n) + " ", end = '')
            print(math.trunc(var / float(2)) - 1 + " ", end = '')
            print(math.trunc(var / float(2)) + " ")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 22
        GFG.evaluate(n)
