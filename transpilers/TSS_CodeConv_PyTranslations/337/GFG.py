import math

class GFG:
    @staticmethod
    def findGreater(a, b):
        x = float(a) * float((math.log(float((b)))))
        y = float(b) * float((math.log(float((a)))))
        if y > x:
            print("a^b is greater")
        elif y < x:
            print("b^a is greater")
        else:
            print("Both are equal")
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = 3
        b = 5
        c = 2
        d = 4
        GFG.findGreater(a, b)
        GFG.findGreater(c, d)
