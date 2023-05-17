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

    numerator = 0
    denominator = 0
    maxproduct = 0
    parts = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = java.util.Scanner(System.in)
        while True:
            Main.numerator = sc.nextInt()
            Main.denominator = sc.nextInt()
            Main.maxproduct = sc.nextInt()
            Main.parts = sc.nextInt()
            if Main.parts == 0:
                break
            count = 0
            count += Main.Judge(Main.numerator, Main.denominator, Main.parts, 1, 0)
            print(count)
    @staticmethod
    def Judge(p, q, separate, now_pro, prev_deno):
        count = 0
        if p == 0:
            count += 1
        if separate <= 0:
            return count
        deno = math.trunc(Main.maxproduct / float(now_pro)) + 1
        while separate * q < p * deno:
            deno -= 1
        while p * deno >= q and prev_deno <= deno:
            subtraction_deno = q * deno
            subtraction_nume = p * deno - q
            if now_pro * deno <= Main.maxproduct:
                count += Main.Judge(subtraction_nume, subtraction_deno, separate - 1, now_pro * deno, deno)
            deno -= 1
        return count
