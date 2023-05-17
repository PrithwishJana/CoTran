class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def nthTerm(N):
        nth = 0
        i = 0
        for i in range(N, 0, -1):
            nth += i ** i
        return nth
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 3
        print(GFG.nthTerm(N))
