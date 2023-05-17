import math

class GFG:
    TEN = 10
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def digitSum(n):
        sum = 0
        while n > 0:
            sum += math.fmod(n, GFG.TEN)
            n = math.trunc(n / float(GFG.TEN))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def getNthTerm(n):
        sum = GFG.digitSum(n)
        if math.fmod(sum, GFG.TEN) == 0:
            return (n * GFG.TEN)
        extra = GFG.TEN - (math.fmod(sum, GFG.TEN))
        return ((n * GFG.TEN) + extra)
    @staticmethod
    def firstNTerms(n):
        for i in range(1, n + 1):
            print(str(GFG.getNthTerm(i)) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 10
        GFG.firstNTerms(n)
