class GFG:
    @staticmethod
    def AvgofSquareN(n):
        sum = 0
        for i in range(1, n + 1):
            sum += (i * i)
        return sum / n
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        print(GFG.AvgofSquareN(n))
