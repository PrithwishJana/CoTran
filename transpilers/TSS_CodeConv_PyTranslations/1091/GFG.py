class GFG:
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
    def count_of_subarrays(N):
        count = GFG.binomialCoeff(2 * N - 1, N)
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        print(str(GFG.count_of_subarrays(N)) + "\n", end = '')
