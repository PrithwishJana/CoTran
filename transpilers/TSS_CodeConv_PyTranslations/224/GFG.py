class GFG:
    @staticmethod
    def hollowSquare(rows):
        i = 0
        j = 0
        for i in range(1, rows + 1):
            if i == 1 or i == rows:
                for j in range(1, rows + 1):
                    print("*", end = '')
            else:
                for j in range(1, rows + 1):
                    if j == 1 or j == rows:
                        print("*", end = '')
                    else:
                        print(" ", end = '')
            print("\n", end = '')
    @staticmethod
    def solidSquare(rows):
        i = 0
        j = 0
        for i in range(1, rows + 1):
            for j in range(1, rows + 1):
                print("*", end = '')
            print("\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def printPattern(rows):
        print("Solid Square:\n", end = '')
        GFG.solidSquare(rows)
        print("\nHollow Square:\n", end = '')
        GFG.hollowSquare(rows)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        rows = 5
        GFG.printPattern(rows)
