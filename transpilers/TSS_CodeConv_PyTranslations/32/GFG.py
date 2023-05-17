class GFG:
    @staticmethod
    def russianPeasant(a, b):
        res = 0
        while b > 0:
            if (b & 1) != 0:
                res = res + a
            a = a << 1
            b = b >> 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.russianPeasant(18, 1))
        print(GFG.russianPeasant(20, 12))
