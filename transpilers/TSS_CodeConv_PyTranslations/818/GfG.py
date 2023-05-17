import math

class GfG:
    @staticmethod
    def digSum(n):
        sum = 0
        while n > 0 or sum > 9:
            if n == 0:
                n = sum
                sum = 0
            sum += math.fmod(n, 10)
            n = math.trunc(n / float(10))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(argc):
        n = 1234
        print(GfG.digSum(n))
