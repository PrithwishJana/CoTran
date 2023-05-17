import math

class GFG:
    @staticmethod
    def subsetXOR(arr, n, K):
        max_ele = arr [0]
        for i in range(1, n):
            if arr [i] > max_ele:
                max_ele = arr [i]
#JAVA TO PYTHON CONVERTER TASK: Java to Python Converter cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
        m = (1 << int((math.log(max_ele) / math.log(2) + 1))) - 1
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    dp [i][j][k] = 0
        for i in range(0, n + 1):
            dp [i][0][0] = 1
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    dp [i][j][k] = dp [i - 1][j][k]
                    if k != 0:
                        dp [i][j][k] += k * dp [i - 1][j ^ arr [i - 1]][k - 1]
        ans = 0
        for i in range(1, n + 1):
            ans += dp [n][K][i]
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3]
        k = 1
        n = len(arr)
        print(GFG.subsetXOR(arr, n, k))
