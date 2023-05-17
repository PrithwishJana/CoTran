class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def fact(N):
        i = 0
        product = 1
        for i in range(1, N + 1):
            product = product * i
        return product
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nthTerm(N):
        return (N * N) * GFG.fact(N)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 4
        print(GFG.nthTerm(N))
