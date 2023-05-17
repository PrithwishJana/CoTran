import math

class GFG:
    @staticmethod
    def divisibleby37(n1):
        l = len(n1)
        if n1 is "0":
            return 0
        if math.fmod(l, 3) == 1:
            n1 = "00" + n1
            l += 2
        elif math.fmod(l, 3) == 2:
            n1 = "0" + n1
            l += 1
        n = n1.toCharArray()
        gSum = 0
        while l != 0:
            gvalue = 0
            if l == 2:
                gvalue = (ord(n [(l - 2)]) - 48) * 100 + (ord(n [(l - 1)]) - 48) * 10
            elif l == 1:
                gvalue = (ord(n [(l - 1)]) - 48) * 100
            else:
                gvalue = (ord(n [(l - 3)]) - 48) * 100 + (ord(n [(l - 2)]) - 48) * 10 + (ord(n [(l - 1)]) - 48) * 1
            l = l - 3
            gSum = gSum + gvalue
        if gSum >= 1000:
            return (GFG.divisibleby37(str(gSum)))
        else:
            return 1 if (math.fmod(gSum, 37) == 0) else 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "8955795758"
        if GFG.divisibleby37(s) == 1:
            print("True")
        else:
            print("False")
