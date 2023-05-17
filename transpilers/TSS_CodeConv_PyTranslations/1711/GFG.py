import math

class GFG:
    @staticmethod
    def minInsertions(H, n, K):
        inser = 0
        for i in range(1, n):
            diff = abs(H [i] - H [i - 1])
            if diff <= K:
                continue
            else:
                inser += math.ceil(diff / K) - 1
        return inser
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        H = [2, 4, 8, 16]
        K = 3
        n = len(H)
        print(GFG.minInsertions(H, n, K))
