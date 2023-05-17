class GFG:
    @staticmethod
    def wastedWater(V, M, N):
        wasted_amt = 0
        amt_per_min = 0
        time_to_fill = 0
        amt_per_min = M - N
        time_to_fill = V / amt_per_min
        wasted_amt = N * time_to_fill
        return wasted_amt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        V = 0
        M = 0
        N = 0
        V = 700
        M = 10
        N = 3
        print(GFG.wastedWater(V, M, N))
        V = 1000
        M = 100
        N = 50
        print(GFG.wastedWater(V, M, N))
