import math

class GFG:
    @staticmethod
    def isTriangular(num):
        if num < 0:
            return False
        c = (- 2 * num)
        b = 1
        a = 1
        d = (b * b) - (4 * a * c)
        if d < 0:
            return False
        root1 = (- b + float(math.sqrt(d))) / (2 * a)
        root2 = (- b - float(math.sqrt(d))) / (2 * a)
        if root1 > 0 and math.floor(root1) == root1:
            return True
        if root2 > 0 and math.floor(root2) == root2:
            return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        num = 55
        if GFG.isTriangular(num):
            print("The number is" + " a triangular number")
        else:
            print("The number " + "is NOT a triangular number")
