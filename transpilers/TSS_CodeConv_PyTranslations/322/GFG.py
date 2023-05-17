class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def sumOfAP(a, d, n):
        sum = 0
        for i in range(0, n):
            sum = sum + a
            a = a + d
        return sum
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = 20
        a = 2.5f
        d = 1.5f
        print(GFG.sumOfAP(a, d, n))
