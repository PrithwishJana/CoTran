class GFG:
    @staticmethod
    def printKPFNums(A, B, K):
        prime = [False for _ in range(B + 1)]
        Arrays.fill(prime, True)
        p_factors = [0 for _ in range(B + 1)]
        Arrays.fill(p_factors, 0)
        for p in range(2, B + 1):
            if p_factors [p] == 0:
                for i in range(p, B + 1, p):
                    p_factors [i] += 1
        for i in range(A, B + 1):
            if p_factors [i] == K:
                print(str(i) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = 14
        B = 18
        K = 2
        GFG.printKPFNums(A, B, K)
