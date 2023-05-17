class GFG:
    @staticmethod
    def longestAlternatingSubarray(a, n):
        longest = 1
        cnt = 1
        for i in range(1, n):
            if a [i] * a [i - 1] < 0:
                cnt += 1
                longest = max(longest, cnt)
            else:
                cnt = 1
        return longest
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [- 5, - 1, - 1, 2, - 2, - 3]
        n = len(a)
        print(GFG.longestAlternatingSubarray(a, n))
