class GFG:
    MX = 2001
    OFF = 1000
    class point:
        def __init__(self, x, y):
            #instance fields found by Java to Python Converter:
            self.x = 0
            self.y = 0

            self.x = x
            self.y = y
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPoints(n, points):
        minx = [0 for _ in range(GFG.MX)]
        miny = [0 for _ in range(GFG.MX)]
        for i in range(0, n):
            minx [i] = Integer.MAX_VALUE
            miny [i] = Integer.MAX_VALUE
        maxx = [0 for _ in range(GFG.MX)]
        maxy = [0 for _ in range(GFG.MX)]
        x = 0
        y = 0
        for i in range(0, n):
            points [i].x += GFG.OFF
            points [i].y += GFG.OFF
            x = points [i].x
            y = points [i].y
            minx [y] = min(minx [y], x)
            maxx [y] = max(maxx [y], x)
            miny [x] = min(miny [x], y)
            maxy [x] = max(maxy [x], y)
        count = 0
        for i in range(0, n):
            x = points [i].x
            y = points [i].y
            if x > minx [y] and x < maxx [y]:
                if y > miny [x] and y < maxy [x]:
                    count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        points = [point(0, 0), point(0, 1), point(1, 0), point(0, - 1), point(- 1, 0)]
        n = len(points)
        print(GFG.countPoints(n, points))
