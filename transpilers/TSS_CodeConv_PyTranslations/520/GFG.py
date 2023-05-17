class GFG:
    @staticmethod
    def countOddNumber(row_num):
        count = 0
        while row_num > 0:
            count += row_num & 1
            row_num >>= 1
        return (1 << count)
    @staticmethod
    def gouldSequence(n):
        for row_num in range(0, n):
            print(str(GFG.countOddNumber(row_num)) + " ", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 16
        GFG.gouldSequence(n)
