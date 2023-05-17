class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(n):
        sum = 0
        for i in range(0, n):
            sum += i * (n - i)
        return 2 * sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.findSum(n))
