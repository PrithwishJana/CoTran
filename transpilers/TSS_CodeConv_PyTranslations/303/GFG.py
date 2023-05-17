class GFG:
    @staticmethod
    def countgroup(a, n):
        xs = 0
        for i in range(0, n):
            xs = xs ^ a [i]
        if xs == 0:
            return (1 << (n - 1)) - 1
        return 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 2, 3]
        n = len(a)
        print(GFG.countgroup(a, n))
