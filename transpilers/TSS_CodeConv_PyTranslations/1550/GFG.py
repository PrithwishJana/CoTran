class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(N, K):
        combo = None
        combo = [0 for _ in range(50)]
        combo [0] = 1
        for i in range(1, K + 1):
            for j in range(0, N + 1):
                if j >= i:
                    combo [j] += combo [j - i]
        return combo [N]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 29
        K = 5
        print(GFG.solve(N, K))
        GFG.solve(N, K)
