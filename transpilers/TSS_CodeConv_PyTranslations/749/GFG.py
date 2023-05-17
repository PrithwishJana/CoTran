class GFG:
    @staticmethod
    def bit_check(n):
        if (n & (n - 1)) == 0:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 14
        if GFG.bit_check(n):
            print('1')
        else:
            print('0')
