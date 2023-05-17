import math

class GFG:
    @staticmethod
    def countOperations(n):
        i = 2
        while (i * i) < n and (math.fmod(n, i)) > 0:
            i += 1
        if (i * i) > n:
            i = n
        return (1 + math.trunc((n - i) / float(2)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print(GFG.countOperations(n))
