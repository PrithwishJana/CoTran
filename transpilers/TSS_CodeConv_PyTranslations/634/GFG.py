class GFG:
    @staticmethod
    def center_hexadecagonal_num(n):
        return 8 * n * n - 8 * n + 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2
        print(str(n) + "th centered " + "hexadecagonal number: ", end = '')
        print(GFG.center_hexadecagonal_num(n))
        n = 12
        print(str(n) + "th centered " + "hexadecagonal number: ", end = '')
        print(GFG.center_hexadecagonal_num(n))
