import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSubarrays(a, n, x):
        count = 0
        number = 0
        for i in range(0, n):
            if a [i] > x:
                count += 1
            else:
                number += math.trunc((count) * (count + 1) / float(2))
                count = 0
        if count != 0:
            number += math.trunc((count) * (count + 1) / float(2))
        return number
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [3, 4, 5, 6, 7, 2, 10, 11]
        n = len(a)
        k = 5
        print(GFG.countSubarrays(a, n, k))
