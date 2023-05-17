import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isPower(n):
        x = 2
        while x <= math.sqrt(n):
            p = x
            while p <= n:
                p = p * x
                if p == n:
                    return True
            x += 1
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        for i in range(2, 100):
            if GFG.isPower(i):
                print(str(i) + " ", end = '')
