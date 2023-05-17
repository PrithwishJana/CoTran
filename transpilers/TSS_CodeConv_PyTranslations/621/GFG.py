import math

class GFG:
    @staticmethod
    def getProduct(n):
        product = 1
        while n != 0:
            product = product * (math.fmod(n, 10))
            n = math.trunc(n / float(10))
        return product
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4513
        print(GFG.getProduct(n))
