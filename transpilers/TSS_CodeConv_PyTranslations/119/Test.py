import math

class Test:
    @staticmethod
    def findMajority(arr, n):
        return arr [math.trunc(n / float(2))]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 2, 3]
        n = len(arr)
        print(Test.findMajority(arr, n))
