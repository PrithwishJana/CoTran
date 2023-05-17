class GFG:
    @staticmethod
    def D_Pattern(n):
        for i in range(0, n):
            for j in range(0, n + 1):
                if j == 1 or ((i == 0 or i == n - 1) and (j > 1 and j < n - 2)) or (j == n - 2 and i != 0 and i != n - 1):
                    print("*", end = '')
                else:
                    print(" ", end = '')
            print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 9
        GFG.D_Pattern(n)
