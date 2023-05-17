import math

class GFG:
    @staticmethod
    def finalNum(arr, n):
        result = 0
        for i in range(0, n):
            result = GFG.__gcd(result, arr [i])
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        return a if b == 0 else GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 9, 6, 36]
        n = len(arr)
        print(GFG.finalNum(arr, n))
