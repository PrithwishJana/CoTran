class GFG:
    @staticmethod
    def printDistSum(arr, n):
        sum = 0
        for i in range(0, n):
            sum += arr [i]
        dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            dp [i][0] = True
        for i in range(1, n + 1):
            dp [i][arr [i - 1]] = True
            for j in range(1, sum + 1):
                if dp [i - 1][j] == True:
                    dp [i][j] = True
                    dp [i][j + arr [i - 1]] = True
        for j in range(0, sum + 1):
            if dp [n][j] == True:
                print(str(j) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [2, 3, 4, 5, 6]
        n = len(arr)
        GFG.printDistSum(arr, n)
