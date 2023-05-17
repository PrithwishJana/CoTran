import math

class Solution:
    @staticmethod
    def minimumX(n, k):
        ans = Integer.MAX_VALUE
        for rem in range(k - 1, 0, -1):
            if math.fmod(n, rem) == 0:
                ans = min(ans, rem + (math.trunc(n / float(rem))) * k)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        k = 6
        print(Solution.minimumX(n, k))
        n = 5
        k = 5
        print(Solution.minimumX(n, k))
