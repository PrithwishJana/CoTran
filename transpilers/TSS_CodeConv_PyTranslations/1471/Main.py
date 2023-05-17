class solution:
    @staticmethod
    def SellingPrice(CP, PP):
        P_decimal = 1 + (PP / 100)
        res = P_decimal * CP
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        C = 720
        P = 13
        print(solution.SellingPrice(C, P))
