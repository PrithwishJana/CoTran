import math

class GFG:
    @staticmethod
    def findN(k):
        ans = 0
        if k == 0:
            ans = 3
        if k == 1:
            ans = 1
        elif math.fmod(k, 4) == 0:
            ans = k
        elif math.fmod(k, 4) == 3:
            ans = k - 1
        else:
            ans = - 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        k = 7
        res = GFG.findN(k)
        if res == - 1:
            print("Not possible")
        else:
            print(res)
