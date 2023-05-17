class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fourthPowerSum(n):
        sum = 0
        for i in range(1, n + 1):
            sum = sum + (i * i * i * i)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 6
        print(GFG.fourthPowerSum(n))
