import math

class GFG:
    @staticmethod
    def printSubstrings(n):
        s = int(math.log10(n))
        d = int((10 ** s + 0.5))
        k = d
        while n > 0:
            while d > 0:
                print(math.trunc(n / float(d)))
                d = math.trunc(d / float(10))
            n = math.fmod(n, k)
            k = math.trunc(k / float(10))
            d = k
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 123
        GFG.printSubstrings(n)
