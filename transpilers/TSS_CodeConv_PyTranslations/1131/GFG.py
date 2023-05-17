class GFG:
    @staticmethod
    def isRectangle(a, b, c, d):
        if a == b and a == c and a == d and c == d and b == c and b == d:
            return True
        elif a == b and c == d:
            return True
        elif a == d and c == b:
            return True
        elif a == c and d == b:
            return True
        else:
            return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 1
        b = 2
        c = 3
        d = 4
        if GFG.isRectangle(a, b, c, d):
            print("Yes")
        else:
            print("No")
