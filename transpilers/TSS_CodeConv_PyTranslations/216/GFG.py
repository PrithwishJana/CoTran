import math

class GFG:
    @staticmethod
    def findWeights(X):
        sum = 0
        power = 0
        number = 3
        while sum < X:
            sum = number - 1
            sum = math.trunc(sum / float(2))
            power += 1
            number *= 3
        ans = 1
        for i in range(1, power + 1):
            print(str(ans) + " ", end = '')
            ans = ans * 3
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        X = 2
        GFG.findWeights(X)
