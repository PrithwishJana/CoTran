class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(A, n):
        dp = [[0 for _ in range(2000)] for _ in range(2000)]
        flag = 1
        sum = 0
        for i in range(0, n):
            sum += A [i]
        for i in range(- sum, sum + 1):
            try:
                dp [0][i] = Integer.MAX_VALUE
            except Exception as e:
                pass
        dp [0][0] = 0
        for i in range(1, n + 1):
            for j in range(0, sum + 1):
                try:
                    dp [flag][j] = Integer.MAX_VALUE
                    if j - A [i - 1] <= sum and j - A [i - 1] >= - sum:
                        dp [flag][j] = dp [flag ^ 1][j - A [i - 1]]
                    if j + A [i - 1] <= sum and j + A [i - 1] >= - sum and dp [flag ^ 1][j + A [i - 1]] != Integer.MAX_VALUE:
                        dp [flag][j] = min(dp [flag][j], dp [flag ^ 1][j + A [i - 1]] + 1)
                except Exception as e:
                    pass
            flag = flag ^ 1
        for i in range(0, sum + 1):
            if dp [flag ^ 1][i] != Integer.MAX_VALUE:
                return dp [flag ^ 1][i]
        return n - 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [10, 22, 9, 33, 21, 50, 41, 60]
        n = len(arr)
        print(GFG.solve(arr, n))
