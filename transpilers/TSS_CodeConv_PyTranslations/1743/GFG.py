class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findNumbers(n, w):
        x = 0
        sum = 0
        if w >= 0 and w <= 8:
            x = 9 - w
        elif w >= - 9 and w <= - 1:
            x = 10 + w
        sum = int(10) ** (n - 2)
        sum = (x * sum)
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 0
        w = 0
        n = 3
        w = 4
        print(GFG.findNumbers(n, w))
