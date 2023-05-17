import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findMin(a, n):
        sum = 0
        for i in range(0, n):
            sum += math.log(a [i])
        x = int(math.exp(sum / n))
        return x + 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [3, 2, 1, 4]
        n = len(a)
        print(GFG.findMin(a, n))
