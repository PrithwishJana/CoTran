import math

class GFG:
    @staticmethod
    def isSumOfPowersOfTwo(n):
        if math.fmod(n, 2) == 1:
            return False
        else:
            return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        if GFG.isSumOfPowersOfTwo(n):
            print("Yes", end = '')
        else:
            print("No", end = '')
