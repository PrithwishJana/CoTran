import math

class GFG:
    COST = 3
    @staticmethod
    def maxItems(x, y, z):
        type1 = math.trunc(x / float(GFG.COST))
        x = math.fmod(x, GFG.COST)
        type2 = math.trunc(y / float(GFG.COST))
        y = math.fmod(y, GFG.COST)
        type3 = math.trunc(z / float(GFG.COST))
        z = math.fmod(z, GFG.COST)
        type4 = min(x, min(y, z))
        maxItems = type1 + type2 + type3 + type4
        return maxItems
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 4
        y = 5
        z = 6
        print(GFG.maxItems(x, y, z))
