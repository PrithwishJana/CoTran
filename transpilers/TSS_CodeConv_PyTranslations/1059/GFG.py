class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def pattern(rows_no):
        i = 0
        j = 0
        k = 0
        for i in range(1, rows_no + 1):
            for k in range(1, i):
                print(" ", end = '')
            for j in range(i, rows_no + 1):
                print(str(j) + " ", end = '')
            print()
        for i in range(rows_no - 1, 0, -1):
            for k in range(1, i):
                print(" ", end = '')
            for j in range(i, rows_no + 1):
                print(str(j) + " ", end = '')
            print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        rows_no = 7
        GFG.pattern(rows_no)
