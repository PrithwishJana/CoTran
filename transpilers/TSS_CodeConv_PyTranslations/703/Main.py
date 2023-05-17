import math

class LIS:
    @staticmethod
    def CeilIndex(A, l, r, key):
        while r - l > 1:
            m = l + math.trunc((r - l) / float(2))
            if A [m] >= key:
                r = m
            else:
                l = m
        return r
    @staticmethod
    def LongestIncreasingSubsequenceLength(A, size):
        tailTable = [0 for _ in range(size)]
        len = 0
        tailTable [0] = A [0]
        len = 1
        for i in range(1, size):
            if A [i] < tailTable [0]:
                tailTable [0] = A [i]
            elif A [i] > tailTable [len - 1]:
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: tailTable [len ++] = A [i];
                tailTable [len ] = A [i]
                len += 1
            else:
                tailTable [LIS.CeilIndex(tailTable, - 1, len - 1, A [i])] = A [i]
        return len
    @staticmethod
    def main(args):
        A = [2, 5, 3, 7, 11, 8, 10, 13, 6]
        n = len(A)
        print("Length of Longest Increasing Subsequence is " + str(LIS.LongestIncreasingSubsequenceLength(A, n)))
