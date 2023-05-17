import math

class GFG:
    @staticmethod
    def countKdivPairs(A, n, K):
        freq = [0 for _ in range(K)]
        ans = 0
        for i in range(0, n):
            rem = math.fmod(A [i], K)
            if rem != 0:
                ans += freq [K - rem]
            else:
                ans += freq [0]
            freq [rem] += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = [2, 2, 1, 7, 5, 3]
        n = len(A)
        K = 4
        print(GFG.countKdivPairs(A, n, K))
