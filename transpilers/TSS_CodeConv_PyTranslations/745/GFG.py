class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def Max_Sum(a, n):
        b = [0 for _ in range(n)]
        S = 0
        res = 0
        for i in range(0, n):
            b [i] = res
            res += a [i]
            S += a [i]
            res = max(res, - S)
        ans = S
        ans = max(ans, res)
        g = 0
        for i in range(n - 1, -1, -1):
            g -= a [i]
            ans = max(ans, g + b [i])
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [- 6, 10, - 3, 10, - 2]
        n = len(a)
        print("Maximum sum is: " + str(GFG.Max_Sum(a, n)))
