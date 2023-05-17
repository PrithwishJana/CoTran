class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nthTerm(N):
        return abs(N * ((N - 1) * (N - 3) * (N - 5)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 6
        print(GFG.nthTerm(N))
