class GFG:
    @staticmethod
    def count_numbers(k, n):
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]
        dp [1][0] = 0
        dp [1][1] = k - 1
        for i in range(2, n + 1):
            dp [i][0] = dp [i - 1][1]
            dp [i][1] = (dp [i - 1][0] + dp [i - 1][1]) * (k - 1)
        return dp [n][0] + dp [n][1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 10
        n = 3
        print(GFG.count_numbers(k, n))
