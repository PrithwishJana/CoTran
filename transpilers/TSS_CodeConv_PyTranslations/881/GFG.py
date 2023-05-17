import math

class GFG:
    @staticmethod
    def decToHexa(n):
        hexaDeciNum = ['\0' for _ in range(100)]
        i = 0
        while n != 0:
            temp = 0
            temp = math.fmod(n, 16)
            if temp < 10:
                hexaDeciNum [i] = chr((temp + 48))
                i += 1
            else:
                hexaDeciNum [i] = chr((temp + 55))
                i += 1
            n = math.trunc(n / float(16))
        for j in range(i - 1, -1, -1):
            print(hexaDeciNum [j], end = '')
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 2545
        GFG.decToHexa(n)
