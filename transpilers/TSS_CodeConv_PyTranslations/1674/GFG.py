import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def count_pairs(a, b, n, m):
        odd1 = 0
        even1 = 0
        odd2 = 0
        even2 = 0
        for i in range(0, n):
            if math.fmod(a [i], 2) == 1:
                odd1 += 1
            else:
                even1 += 1
        for i in range(0, m):
            if math.fmod(b [i], 2) == 1:
                odd2 += 1
            else:
                even2 += 1
        pairs = min(odd1, even2) + min(odd2, even1)
        return pairs
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [9, 14, 6, 2, 11]
        b = [8, 4, 7, 20]
        n = len(a)
        m = len(b)
        print(GFG.count_pairs(a, b, n, m))
