import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getTotalXorOfSubarrayXors(arr, N):
        res = 0
        for i in range(0, N):
            freq = (i + 1) * (N - i)
            if math.fmod(freq, 2) == 1:
                res = res ^ arr [i]
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 5, 2, 4, 6]
        N = len(arr)
        print(GFG.getTotalXorOfSubarrayXors(arr, N))
