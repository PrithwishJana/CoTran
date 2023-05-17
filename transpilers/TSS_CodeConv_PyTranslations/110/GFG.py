class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxSubArraySum(a, size):
        max_so_far = Integer.MIN_VALUE
        max_ending_here = 0
        for i in range(0, size):
            max_ending_here = max_ending_here + a [i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
    @staticmethod
    def minPossibleSum(a, n, x):
        mxSum = GFG.maxSubArraySum(a, n)
        sum = 0
        for i in range(0, n):
            sum += a [i]
        sum = sum - mxSum + mxSum / x
        print(str(sum) + "\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        X = 2
        A = [1, - 2, 3]
        GFG.minPossibleSum(A, N, X)
