import math

class GFG:
    @staticmethod
    def findCountOfPairs(a, b, n):
        ans = 0
        ans += n * (math.trunc(a / float(n))) * (math.trunc(b / float(n)))
        ans += (math.trunc(a / float(n))) * (math.fmod(b, n))
        ans += (math.fmod(a, n)) * (math.trunc(b / float(n)))
        ans += math.trunc(((math.fmod(a, n)) + (math.fmod(b, n))) / float(n))
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 5
        b = 13
        n = 3
        print(GFG.findCountOfPairs(a, b, n))
