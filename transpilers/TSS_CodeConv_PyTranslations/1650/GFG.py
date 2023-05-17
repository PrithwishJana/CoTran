import math

class GFG:
    @staticmethod
    def properDivisorSum(n):
        sum = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if math.fmod(i, j) == 0:
                    if math.trunc(i / float(j)) == j:
                        sum += j
                    else:
                        sum += j + math.trunc(i / float(j))
                j += 1
            sum = sum - i
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        print(GFG.properDivisorSum(n))
        n = 5
        print(GFG.properDivisorSum(n))
