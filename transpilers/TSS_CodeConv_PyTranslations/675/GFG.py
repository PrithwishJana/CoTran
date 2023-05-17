import math

class GFG:
    @staticmethod
    def rmsValue(arr, n):
        square = 0
        mean = 0
        root = 0
        for i in range(0, n):
            square += arr [i] ** 2
        mean = (square / float((n)))
        root = float(math.sqrt(mean))
        return root
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 4, 6, 8]
        n = len(arr)
        print("{0:.4f}".format(GFG.rmsValue(arr, n)))
