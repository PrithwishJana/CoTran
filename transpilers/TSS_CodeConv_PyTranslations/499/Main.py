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

    dp = None
    knaps = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = Scanner(System.in)
        n = sc.nextInt()
        w = sc.nextInt()
        Main.knaps = [None for _ in range(n)]
        for i in range(0, n):
            Main.knaps [i] = Knap(sc.nextInt(), sc.nextInt())
        Arrays.sort(Main.knaps)
        Main.dp = [[0 for _ in range(w + 1)] for _ in range(n)]
        print(Main.dfw(n - 1, w))
    @staticmethod
    def dfw(idx, weight):
        if weight < 0:
            return Integer.MIN_VALUE
        if idx < 0:
            return 0
        if Main.dp [idx][weight] != 0:
            return Main.dp [idx][weight]
        if math.fmod(weight, Main.knaps [idx].weight) == 0:
            return Main.dp [idx][weight] = math.trunc(weight / float(Main.knaps [idx].weight * Main.knaps [idx].value))
        max = 0
        i = 0
        while i * Main.knaps [idx].weight <= weight:
            max = max(max, Main.dfw(idx - 1, weight - Main.knaps [idx].weight * i) + Main.knaps [idx].value * i)
            i += 1
        return Main.dp [idx][weight] = max
    class Knap(Comparable):
        def __init__(self, value, weight):
            #instance fields found by Java to Python Converter:
            self.value = 0
            self.weight = 0

            self.value = value
            self.weight = weight
        def compareTo(self, another):
            return self.value * another.weight - another.value * self.weight
