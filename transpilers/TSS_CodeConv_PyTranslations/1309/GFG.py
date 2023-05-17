class GFG:
    @staticmethod
    def sumOfSeries(n):
        sum = 0
        for i in range(1, n + 1):
            sum = sum + (2 * i - 1) * (2 * i - 1)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        print(GFG.sumOfSeries(n))
