class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculateSum(n):
        sum = 0
        for row in range(0, n):
            sum = sum + (1 << row)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        print("Sum of all elements:" + str(GFG.calculateSum(n)))
