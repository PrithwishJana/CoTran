class GFG:
    @staticmethod
    def findQuadruples(a, b, c, d, x, n):
        count = 0
        for i in range(0, n):
            for j in range(0, n):
                for k in range(0, n):
                    for l in range(0, n):
                        if (a [i] ^ b [j] ^ c [k] ^ d [l]) == x:
                            count += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        x = 3
        a = [0, 1]
        b = [2, 0]
        c = [0, 1]
        d = [0, 1]
        n = len(a)
        print(GFG.findQuadruples(a, b, c, d, x, n))
