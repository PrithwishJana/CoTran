class GFG:
    @staticmethod
    def max_sum(a, n):
        dp = [0 for _ in range(n)]
        if n == 1:
            dp [0] = max(0, a [0])
        elif n == 2:
            dp [0] = max(0, a [0])
            dp [1] = max(a [1], dp [0])
        elif n >= 3:
            dp [0] = max(0, a [0])
            dp [1] = max(a [1], max(0, a [0]))
            dp [2] = max(a [2], max(a [1], max(0, a [0])))
            i = 3
            while i < n:
                dp [i] = max(dp [i - 1], a [i] + dp [i - 3])
                i += 1
        return dp [n - 1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, - 2, 4, 3]
        n = len(arr)
        print(GFG.max_sum(arr, n))
