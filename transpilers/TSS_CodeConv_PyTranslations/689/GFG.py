import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isDivisible(n):
        temp = n
        sum = 0
        while n != 0:
            k = math.fmod(int(n), 10)
            sum += k
            n = math.trunc(n / float(10))
        if math.fmod(temp, sum) == 0:
            return "YES"
        return "NO"
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 123
        print(GFG.isDivisible(n))
