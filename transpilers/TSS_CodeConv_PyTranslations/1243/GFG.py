class GFG:
    @staticmethod
    def catalanDP(n):
        catalan = [0 for _ in range(n + 2)]
        catalan [0] = 1
        catalan [1] = 1
        for i in range(2, n + 1):
            catalan [i] = 0
            for j in range(0, i):
                catalan [i] += catalan [j] * catalan [i - j - 1]
        return catalan [n]
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        for i in range(0, 10):
            print(str(GFG.catalanDP(i)) + " ", end = '')
