class GFG:
    class Point:
        def __init__(self, x, y):
            #instance fields found by Java to Python Converter:
            self.x = 0
            self.y = 0

            self.x = x
            self.y = y
    @staticmethod
    def findmin(p, n):
        a = 0
        b = 0
        c = 0
        d = 0
        for i in range(0, n):
            if p [i].x <= 0:
                a += 1
            elif p [i].x >= 0:
                b += 1
            if p [i].y >= 0:
                c += 1
            elif p [i].y <= 0:
                d += 1
        return min(min(a, b), min(c, d))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        p = [Point(1, 1), Point(2, 2), Point(- 1, - 1), Point(- 2, 2)]
        n = len(p)
        print(GFG.findmin(p, n))
