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

    Main.MOD = 1000000007
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = java.util.Scanner(System.in)
        while True:
            aa = sc.next().toCharArray()
            if aa [0] == '0':
                break
            bb = sc.next().toCharArray()
            cc = sc.next().toCharArray()
            n = len(aa)
            dp = [[0 for _ in range(2)] for _ in range(n + 1)]
            dp [0][0] = 1
            for i in range(1, n + 1):
                da = aa [n - i] == '?- 1 if ' else aa [n - i] - '0'
                db = bb [n - i] == '?- 1 if ' else bb [n - i] - '0'
                dc = cc [n - i] == '?- 1 if ' else cc [n - i] - '0'
                for j in range(0, 2):
                    for carry in range(0, 2):
                        patterns = 0
                        for a in range(0, 10):
                            if da != - 1 and da != a:
                                continue
                            for b in range(0, 10):
                                if db != - 1 and db != b:
                                    continue
                                c = a + b + carry
                                if (j == 0 and c >= 10) or (j == 1 and c < 10):
                                    continue
                                if i == n:
                                    if a * b * c == 0:
                                        continue
                                if dc == - 1 or dc == math.fmod(c, 10):
                                    patterns += 1
                        dp [i][j] += math.fmod(dp [i - 1][carry] * patterns, Main.MOD)
                        dp [i][j] = math.fmod(dp [i][j], Main.MOD)
            print(dp [n][0])
