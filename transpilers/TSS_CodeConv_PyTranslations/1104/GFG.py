import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(N, K):
        ans = 0
        for i in range(1, N + 1):
            ans += (math.fmod(i, K))
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 10
        K = 2
        print(GFG.findSum(N, K))
