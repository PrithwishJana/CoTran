import math

class GFG:
    @staticmethod
    def countSubsets(arr, n):
        us = HashSet()
        even_count = 0
        for i in range(0, n):
            if math.fmod(arr [i], 2) == 0:
                us.add(arr [i])
        even_count = us.size()
        return int((2 ** even_count - 1))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 2, 1, 9, 2, 6, 5, 3]
        n = len(arr)
        print("Number of subsets = " + str(GFG.countSubsets(arr, n)))
