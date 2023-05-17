class GFG:
    @staticmethod
    def maximumArea(l, b, x, y):
        left = 0
        right = 0
        above = 0
        below = 0
        left = x * b
        right = (l - x - 1) * b
        above = l * y
        below = (b - y - 1) * l
        print(max(max(left, right), max(above, below)))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = 8
        B = 8
        X = 0
        Y = 0
        GFG.maximumArea(L, B, X, Y)
