class solution:
    @staticmethod
    def pattern(N):
        i = 0
        j = 0
        k = 0
        space = 1
        rows = N
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                print("*", end = '')
            if i != rows:
                for k in range(1, space + 1):
                    print(" ", end = '')
                space = space + 2
            for j in range(i, 0, -1):
                if j != rows:
                    print("*", end = '')
            print("\n", end = '')
        print("\n", end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        N = 6
        solution.pattern(N)
