class GFG:
    @staticmethod
    def longestFibonacciSubarray(n, a):
        if n <= 2:
            return n
        len = 2
        mx = Integer.MIN_VALUE
        for i in range(2, n):
            if a [i] == a [i - 1] + a [i - 2]:
                len += 1
            else:
                len = 2
            mx = max(mx, len)
        return mx
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        a = [2, 4, 6, 10, 2]
        print(GFG.longestFibonacciSubarray(n, a))
