import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isDivisible(n):
        temp = n
        while n > 0:
            k = math.fmod(n, 10)
            if math.fmod(temp, k) == 0:
                return "YES"
            n = math.trunc(n / float(10))
        return "NO"
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 9876543
        print(GFG.isDivisible(n))
