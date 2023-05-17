class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countWays(n):
        dp = [0 for _ in range(n + 1)]
        dp [0] = 0
        dp [1] = 1
        dp [2] = 1
        for i in range(3, n + 1):
            dp [i] = dp [i - 1] + dp [i - 3] + 1
        return dp [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        print(GFG.countWays(n))
