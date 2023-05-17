import math

class Main:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        Main.IN = java.util.Scanner(System.in)
        Main._sc = None
        Main.IN = Scanner(System.in)
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
        Main._sc = Scanner(System.in)
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
        input = Scanner(System.in)
        tc = input.nextInt()
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#        work :
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (tc -- > 0)
        while tc  > 0:
            tc -= 1
            n = input.nextLong()
            x = Long.MAX_VALUE
            y = Long.MIN_VALUE
            if math.fmod(n, 6) == 0:
                x = min(x, math.trunc(n / float(6)))
                y = max(y, math.trunc(n / float(6)))
            if math.fmod(n, 6) == 2 and n != 2:
                x = min(x, ((math.trunc(n / float(6))) - 1) + 2)
                y = max(y, ((math.trunc(n / float(6))) - 1) + 2)
            if math.fmod(n, 6) == 4 and n != 4:
                x = min(x, math.trunc(n / float(6)) + 1)
                y = max(y, math.trunc(n / float(6)) + 1)
            if math.fmod(n, 4) == 0:
                x = min(x, math.trunc(n / float(4)))
                y = max(y, math.trunc(n / float(4)))
            if math.fmod(n, 4) == 2 and n != 2:
                x = min(x, (math.trunc(n / float(4))) - 1 + 1)
                y = max(y, (math.trunc(n / float(4))) - 1 + 1)
            if x != Long.MAX_VALUE and y != Long.MIN_VALUE:
                print(str(x) + " " + str(y))
            else:
                print("-1")
        tc -= 1
