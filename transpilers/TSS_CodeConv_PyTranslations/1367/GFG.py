class GFG:
    PI = 3.142
    @staticmethod
    def cosXSertiesSum(x, n):
        x = x * (GFG.PI / 180.0)
        res = 1
        sign = 1
        fact = 1
        pow = 1
        for i in range(1, 5):
            sign = sign * - 1
            fact = fact * (2 * i - 1) * (2 * i)
            pow = pow * x * x
            res = res + sign * pow / fact
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 50
        n = 5
        print(float((GFG.cosXSertiesSum(x, 5) * 1000000)) / 1000000.00)
