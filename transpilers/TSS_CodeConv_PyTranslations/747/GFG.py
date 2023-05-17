import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def reverse(str, x):
        n = math.trunc((len(str) - x) / float(2))
        for i in range(0, n):
            print(str[i], end = '')
        for i in range(n + x - 1, n - 1, -1):
            print(str[i], end = '')
        i = n + x
        while i < len(str):
            print(str[i], end = '')
            i += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        str = "geeksforgeeks"
        x = 3
        GFG.reverse(str, x)
