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
        sn = java.util.Scanner(System.in)
        while True:
            slot = Slot(sn.nextInt(), sn.nextInt(), sn.nextInt(), sn.nextInt(), sn.nextInt(), sn.nextInt())
            if slot.isEnd():
                break
            print(100 + slot.getBenefit() - slot.getLost())
class Slot:
    def __init__(self, b, r, g, c, s, t):
        #instance fields found by Java to Python Converter:
        self.b = 0
        self.r = 0
        self.g = 0
        self.c = 0
        self.s = 0
        self.t = 0

        self.b = b
        self.r = r
        self.g = g
        self.c = c
        self.s = s
        self.t = t
    def getLost(self):
        return (self.t - 5 * self.b - 3 * self.r - self.s) * 3 + (5 * self.b + 3 * self.r) * 2
    def getBenefit(self):
        return self.b * 15 + self.r * 15 + self.g * 7 + self.c * 2 + (self.b * 5 + self.r * 3) * 15
    def isEnd(self):
        return self.b + self.r + self.g + self.c + self.s + self.t == 0
