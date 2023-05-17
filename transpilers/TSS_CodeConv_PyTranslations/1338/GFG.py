import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def count(x, y):
        ans = 0
        m = {}
        while math.fmod(x, y) != 0:
            x = math.fmod(x, y)
            ans += 1
            if x in m.keys():
                return - 1
            m[x] = 1
            x = x * 10
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        res = GFG.count(1, 2)
        if (res == - 1):
            print("INF")
        else:
            print(res)
        res = GFG.count(5, 3)
        if (res == - 1):
            print("INF")
        else:
            print(res)
        res = GFG.count(3, 5)
        if (res == - 1):
            print("INF")
        else:
            print(res)
