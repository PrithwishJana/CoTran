import math

class GFG:
    @staticmethod
    def GCD(a, b):
        if b == 0:
            return a
        return GFG.GCD(b, math.fmod(a, b))
    @staticmethod
    def findMaxSumUtil(arr, n):
        finalGCD = arr [0]
        for i in range(1, n):
            finalGCD = GFG.GCD(arr [i], finalGCD)
        return finalGCD
    @staticmethod
    def findMaxSum(arr, n):
        maxElement = GFG.findMaxSumUtil(arr, n)
        return (maxElement * n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [8, 20, 12, 36]
        n = len(arr)
        print(GFG.findMaxSum(arr, n))
