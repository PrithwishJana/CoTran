import math

class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def __gcd(a, b):
        if b == 0:
            return a
        else:
            return GFG.__gcd(b, math.fmod(a, b))
    @staticmethod
    def LCM(x, y, z):
        ans = (math.trunc((x * y) / float(GFG.__gcd(x, y))))
        return (math.trunc((z * ans) / float(GFG.__gcd(ans, z))))
    @staticmethod
    def findDivisible(n, x, y, z):
        lcm = GFG.LCM(x, y, z)
        ndigitnumber = int(10) ** (n - 1)
        reminder = math.fmod(ndigitnumber, lcm)
        if reminder == 0:
            return ndigitnumber
        ndigitnumber += lcm - reminder
        if ndigitnumber < 10 ** n:
            return ndigitnumber
        else:
            return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 4
        x = 2
        y = 3
        z = 5
        res = GFG.findDivisible(n, x, y, z)
        if res != 0:
            print(res)
        else:
            print("Not possible")
