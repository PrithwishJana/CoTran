import math

class GFG:
    @staticmethod
    def complement(num):
        i = 0
        len = 0
        temp = 0
        comp = 0
        temp = num
        while True:
            len += 1
            num = math.trunc(num / float(10))
            if abs(num) == 0:
                break
        num = temp
        comp = int(10) ** len - num
        return comp
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        print(GFG.complement(25))
        print(GFG.complement(456))
