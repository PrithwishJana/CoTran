class GFG:
    MAX = 100000
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def print(g1, a, g2, b):
        for i in range(0, a):
            print(str(g1 [i]) + " ", end = '')
        print("and ", end = '')
        for i in range(0, b):
            print(str(g2 [i]) + " ", end = '')
        print()
    @staticmethod
    def checksum(g1, a, g2, b):
        i = 0
        x = 0
        i = 0
        x = 0
        while i < a:
            x += g1 [i]
            i += 1
        for i in range(0, b):
            x -= g2 [i]
        return (x == 0)
    @staticmethod
    def formgroups(arr, x, g1, a, g2, b, n):
        if x == n:
            if GFG.checksum(g1, a, g2, b):
                GFG.print(g1, a, g2, b)
            return
        g1 [a] = arr [x]
        GFG.formgroups(arr, x + 1, g1, a + 1, g2, b, n)
        g2 [b] = arr [x]
        GFG.formgroups(arr, x + 1, g1, a, g2, b + 1, n)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 2, 3, 9, 4, 5]
        n = len(arr)
        g1 = [0 for _ in range(GFG.MAX)]
        g2 = [0 for _ in range(GFG.MAX)]
        GFG.formgroups(arr, 0, g1, 0, g2, 0, n)
