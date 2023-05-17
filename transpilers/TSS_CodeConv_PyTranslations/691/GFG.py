class GFG:
    @staticmethod
    def calculateAreaSum(l, b):
        size = 1
        maxSize = min(l, b)
        totalArea = 0
        for i in range(1, maxSize + 1):
            totalSquares = (l - size + 1) * (b - size + 1)
            area = totalSquares * size * size
            totalArea += area
            size += 1
        return totalArea
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        l = 4
        b = 3
        print(GFG.calculateAreaSum(l, b))
