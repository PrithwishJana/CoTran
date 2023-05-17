class GFG:
    @staticmethod
    def distancesum(x, y, n):
        sum = 0
        for i in range(0, n):
            for j in range(i + 1, n):
                sum += (abs(x [i] - x [j]) + abs(y [i] - y [j]))
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = [- 1, 1, 3, 2]
        y = [5, 6, 5, 3]
        n = len(x)
        print(GFG.distancesum(x, y, n))
