class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculateSum(n):
        sum = 0
        sum = 1 << n
        return (sum - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        print("Sum of all elements:" + str(GFG.calculateSum(n)))
