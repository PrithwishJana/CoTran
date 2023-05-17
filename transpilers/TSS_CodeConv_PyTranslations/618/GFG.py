class GFG:
    @staticmethod
    def printNumberWithDR(k, d):
        if d == 0 and k != 1:
            print("-1", end = '')
        else:
            print(d, end = '')
            k -= 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (k -- > 0)
            while k  > 0:
                k -= 1
                print("0", end = '')
            k -= 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 4
        d = 4
        GFG.printNumberWithDR(k, d)
