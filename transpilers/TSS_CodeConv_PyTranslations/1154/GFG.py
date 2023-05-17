import math

class GFG:
    N = 1000
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(arr, n):
        size = (2 * GFG.N) + 1
        freq = [0 for _ in range(size)]
        for i in range(0, n):
            x = arr [i]
            freq [x + GFG.N] += 1
        ans = 0
        for i in range(0, size):
            if freq [i] > 0:
                ans += math.trunc(((freq [i]) * (freq [i] - 1)) / float(2))
                for j in range(i + 2, 2001, 2):
                    if freq [j] > 0 and (freq [math.trunc((i + j) / float(2))] > 0):
                        ans += (freq [i] * freq [j])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [4, 2, 5, 1, 3, 5]
        n = len(arr)
        print(GFG.countPairs(arr, n))
