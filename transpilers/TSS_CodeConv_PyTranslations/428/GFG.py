class GFG:
    MAX = 100
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def binomialCoeff(n, k):
        C = [0 for _ in range(k + 1)]
        C [0] = 1
        for i in range(1, n + 1):
            for j in range(min(i, k), 0, -1):
                C [j] = C [j] + C [j - 1]
        return C [k]
    @staticmethod
    def sumOfproduct(n):
        return GFG.binomialCoeff(2 * n, n - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.sumOfproduct(n))
