import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countDivisors(n, k):
        count = 0
        i = 0
        for i in range(1, n + 1):
            if math.fmod(n, i) == 0 and math.fmod(i, k) == 0:
                count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 12
        k = 3
        print(GFG.countDivisors(n, k))
