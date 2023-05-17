import math

class GfG:
    @staticmethod
    def min_noOf_operation(arr, n, k):
        noOfSubtraction = 0
        res = 0
        for i in range(1, n):
            noOfSubtraction = 0
            if arr [i] > arr [i - 1]:
                noOfSubtraction = math.trunc((arr [i] - arr [i - 1]) / float(k))
                if math.fmod((arr [i] - arr [i - 1]), k) != 0:
                    noOfSubtraction += 1
                arr [i] = arr [i] - k * noOfSubtraction
            res = res + noOfSubtraction
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(argc):
        arr = [1, 1, 2, 3]
        N = 4
        k = 5
        print(GfG.min_noOf_operation(arr, N, k))
