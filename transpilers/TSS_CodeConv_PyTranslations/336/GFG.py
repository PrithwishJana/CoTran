import math

class GFG:
    @staticmethod
    def sumOfDigits(x):
        sum = 0
        while x != 0:
            sum += math.fmod(x, 10)
            x = math.trunc(x / float(10))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countNumbers(l, r):
        count = 0
        for i in range(l, r + 1):
            if math.fmod(i, 2) == 0 and math.fmod(GFG.sumOfDigits(i), 3) == 0:
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 1000
        r = 6000
        print(GFG.countNumbers(l, r))
