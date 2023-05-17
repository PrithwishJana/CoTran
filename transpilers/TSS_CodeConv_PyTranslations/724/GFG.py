class GFG:
    @staticmethod
    def fun(n):
        return n & (n - 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(arg):
        n = 7
        print("The number after unsetting " + "the rightmost set bit " + str(GFG.fun(n)), end = '')
