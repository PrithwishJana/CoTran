class GFG:
    @staticmethod
    def expect(m, n):
        ans = 0.0
        i = 0
        for i in range(m, 0, -1):
            ans += ((i / m) ** n - ((i - 1) / m) ** n) * i
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        m = 6
        n = 3
        print("{0:.5f}".format(GFG.expect(m, n)))
