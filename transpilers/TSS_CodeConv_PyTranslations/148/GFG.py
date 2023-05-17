class GFG:
    @staticmethod
    def countIntegralSolutions(n):
        result = 0
        for i in range(0, n + 1):
            j = 0
            while j <= n - i:
                k = 0
                while k <= (n - i - j):
                    if i + j + k == n:
                        result += 1
                    k += 1
                j += 1
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 3
        print(GFG.countIntegralSolutions(n))
