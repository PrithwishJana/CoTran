class GFG:
    @staticmethod
    def findIndex(n):
        if n <= 1:
            return n
        a = 0
        b = 1
        c = 1
        res = 1
        while c < n:
            c = a + b
            res += 1
            a = b
            b = c
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        result = GFG.findIndex(21)
        print(result)
