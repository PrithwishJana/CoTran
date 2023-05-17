import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def multiply(a, b):
        mul = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(0, 3):
            for j in range(0, 3):
                mul [i][j] = 0
                for k in range(0, 3):
                    mul [i][j] += a [i][k] * b [k][j]
        for i in range(0, 3):
            for j in range(0, 3):
                a [i][j] = mul [i][j]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def power(F, n):
        M = [[ 1, 1, 1 ], [ 1, 0, 0 ], [ 0, 1, 0 ]]
        if n == 1:
            return F [0][0] + F [0][1]
        GFG.power(F, math.trunc(n / float(2)))
        GFG.multiply(F, F)
        if math.fmod(n, 2) != 0:
            GFG.multiply(F, M)
        return F [0][0] + F [0][1]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNthTerm(n):
        F = [[ 1, 1, 1 ], [ 1, 0, 0 ], [ 0, 1, 0 ]]
        return GFG.power(F, n - 2)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        print("F(5) is " + GFG.findNthTerm(n))
