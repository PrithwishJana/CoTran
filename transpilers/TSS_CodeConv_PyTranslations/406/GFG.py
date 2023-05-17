import math

class GFG:
    @staticmethod
    def disp(row_no, block):
        print(row_no * block, end = '')
    @staticmethod
    def row(ht, h):
        return math.trunc(ht / float(h))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calculate(l, w, h, a, ht):
        no_block = math.trunc((4 * a) / float(l))
        row_no = 0
        if h < w:
            row_no = GFG.row(ht, w)
        else:
            row_no = GFG.row(ht, h)
        GFG.disp(row_no, no_block)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 50
        w = 20
        h = 35
        a = 700
        ht = 140
        GFG.calculate(l, w, h, a, ht)
