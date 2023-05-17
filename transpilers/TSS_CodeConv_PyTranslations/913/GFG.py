import math

class GFG:
    MOD = 1000000007
    inv2 = 500000004
    @staticmethod
    def modulo(num):
        res = 0
        i = 0
        while i < len(num):
            res = math.fmod((res * 10 + ord(num[i]) - '0'), GFG.MOD)
            i += 1
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def findSum(L, R):
        a = 0
        b = 0
        l = 0
        r = 0
        ret = 0
        a = GFG.modulo(L)
        b = GFG.modulo(R)
        l = math.fmod((math.fmod((a * (a - 1)), GFG.MOD * GFG.inv2)), GFG.MOD)
        r = math.fmod((math.fmod((b * (b + 1)), GFG.MOD * GFG.inv2)), GFG.MOD)
        ret = (math.fmod(r, GFG.MOD) - math.fmod(l, GFG.MOD))
        if ret < 0:
            ret = ret + GFG.MOD
        else:
            ret = math.fmod(ret, GFG.MOD)
        return ret
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        L = "88949273204"
        R = "98429729474298592"
        print(GFG.findSum(L, R))
