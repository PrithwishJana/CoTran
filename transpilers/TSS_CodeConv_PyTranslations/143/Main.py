import math

class Main:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        Main.IN = java.util.Scanner(System.in)
        Main._sc = None
        Main.IN = java.util.Scanner(System.in)
        Main._sc = java.util.Scanner(System.in)
        Main.INF = 1 << 28
        self.EPS = 1e-10
        Main.MOD = 1000000
        self.es = [[ 0, 1, 2, 3 ], [ 0, 1, 2 ], [ 0, 1, 2, 4 ], [ 2, 3 ], [ 0, 4 ]]
        self.len = 5
        self.scan = None
        Main._N = 0
        Main.MOD = 1000000007
        self._node = None
        Main.n = 0
        self.t = [0 for _ in range(10)]
        Main.INF = 1 << 30
        Main._sc = java.util.Scanner(System.in)
        self.EPS = 1e-9
        Main.m = 0
        Main.a = None
        Main._MAX = 'Z' - 'A' + 1
        self.inDeg = None
        self.outDeg = None
        Main.vis = None
        self.nei = None
        Main.INF = Integer.MAX_VALUE
        Main.MOD = 1000000007
        self.TOKENS = ["A", "C", "G", "T"]
        Main.memo = None
        Main._N = 12
        self.ofs = [[ 1, 0 ], [ 0, - 1 ], [ - 1, 0 ], [ 0, 1 ]]
        self.log = None
        self.result = System.out
        self.systemin = None
        self.graph = None
        self.visited = None
        self.color = None
        self.one = 0
        self.bipartite = 0
        Main.count = 0
        self.mujun = False
        self.maxes = None
        self.len = 393
        Main.h = 0
        Main.w = 0
        Main.map = None
        self.v = None
        self.dy = [- 1, - 1, 0, 0, 1, 1]
        self.dx1 = [0, 1, - 1, 1, 0, 1]
        self.dx2 = [- 1, 0, - 1, 1, - 1, 0]
        Main.grid = None
        Main.B = False
        self.W = False
        self.countB = 0
        self.countW = 0
        self.dx = [1, - 1, 0, 0]
        self.dy = [0, 0, 1, - 1]
        self.from_ = '\0'
        self.to = '\0'
        self.countGrid = 0

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        input = java.util.Scanner(System.in)
        r1 = input.nextInt()
        r2 = input.nextInt()
        c1 = input.nextInt()
        c2 = input.nextInt()
        d1 = input.nextInt()
        d2 = input.nextInt()
        if (c1 + c2 - r1 - r2) != 0 or (d1 + d2 - r1 - r2) != 0:
            print(- 1, end = '')
        else:
            flag = True
            t = math.trunc((r2 - d2 + c2) / float(2))
            z = d2 - c2 + t
            y = c2 - t
            x = r1 + r2 - y - z - t
            box = [x, y, z, t]
            for gem in box:
                if gem > 9 or gem < 1:
                    flag = False
                    break
            if (x == y) or (x == z) or (x == t) or (y == z) or (y == t) or (z == t):
                flag = False
            if flag:
#JAVA TO PYTHON CONVERTER TASK: The following line has a Java format specifier which cannot be directly translated to Python:
                print("{0:d} {1:d}%n%d %d".format(x, y, z, t), end = '')
            else:
                print(- 1, end = '')
