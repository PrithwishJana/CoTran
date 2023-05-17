import math

class GFG:
    MAX = 10000
    prodDig = [0 for _ in range(MAX)]
    @staticmethod
    def getDigitProduct(x):
        if x < 10:
            return x
        if GFG.prodDig [x] != 0:
            return GFG.prodDig [x]
        prod = (math.fmod(x, 10)) * GFG.getDigitProduct(math.trunc(x / float(10)))
        return (GFG.prodDig [x] := prod)
    @staticmethod
    def findSeed(n):
        res = []
        i = 1
        while i <= math.trunc(n / float(2)):
            if i * GFG.getDigitProduct(i) == n:
                res.append(i)
            i += 1
        if len(res) == 0:
            print("NO seed exists")
            return
        for i, unusedItem in enumerate(res):
            print(str(res[i]) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 138
        GFG.findSeed(n)
