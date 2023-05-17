import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fact(num):
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def catalan(n):
        return math.trunc(GFG.fact(2 * n) / float(GFG.fact(n) * GFG.fact(n + 1)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 5
        arr = [1, 2, 3, 4, 5]
        i = 0
        k = 0
        for k in range(0, n):
            s = 0
            for i in range(0, n):
                if arr [i] < arr [k]:
                    s += 1
            catalan_leftBST = GFG.catalan(s)
            catalan_rightBST = GFG.catalan(n - s - 1)
            totalBST = catalan_rightBST * catalan_leftBST
            print(str(totalBST) + " ", end = '')
