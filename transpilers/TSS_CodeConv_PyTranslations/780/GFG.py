import math

class GFG:
    @staticmethod
    def longestSubarray(a, n):
        hash = [[0 for _ in range(10)] for _ in range(n)]
        for i in range(0, n):
            num = a [i]
            while num != 0:
                hash [i][math.fmod(num, 10)] = 1
                num = math.trunc(num / float(10))
        longest = Integer.MIN_VALUE
        count = 0
        i = 0
        while i < n - 1:
            j = 0
            for j in range(0, 10):
                if hash [i][j] == 1 & hash [i + 1][j] == 1:
                    count += 1
                    break
            if j == 10:
                longest = max(longest, count + 1)
                count = 0
            i += 1
        longest = max(longest, count + 1)
        return longest
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [11, 22, 33, 44, 54, 56, 63]
        n = len(a)
        print(GFG.longestSubarray(a, n))
