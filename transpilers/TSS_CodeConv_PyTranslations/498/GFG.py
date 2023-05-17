import math

class GFG:
    @staticmethod
    def isMajority(a, n):
        mp = {}
        for i in range(0, n):
            if a [i] in mp.keys():
                mp[a [i]] = mp[a [i]] + 1
            else:
                mp[a [i]] = 1
        for x in mp.entrySet():
            if x.getValue() >= math.trunc(n / float(2)):
                return True
        return False
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [2, 3, 9, 2, 2]
        n = len(a)
        if GFG.isMajority(a, n):
            print("Yes")
        else:
            print("No")
