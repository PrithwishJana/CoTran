import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def negProdSubArr(arr, n):
        positive = 1
        negative = 0
        for i in range(0, n):
            if arr [i] > 0:
                arr [i] = 1
            else:
                arr [i] = - 1
            if i > 0:
                arr [i] *= arr [i - 1]
            if arr [i] == 1:
                positive += 1
            else:
                negative += 1
        return (positive * negative)
    @staticmethod
    def posProdSubArr(arr, n):
        total = math.trunc((n * (n + 1)) / float(2))
        cntNeg = GFG.negProdSubArr(arr, n)
        return (total - cntNeg)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, - 4, - 3, 2, - 5]
        n = len(arr)
        print(GFG.posProdSubArr(arr, n))
