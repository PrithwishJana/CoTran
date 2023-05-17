//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

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

    mod = 998244353
    nchoosek = None
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        Main.nchoosek = [[0 for _ in range(4001)] for _ in range(4001)]
        i = 0
        while i < len(Main.nchoosek):
            Main.nchoosek [i][0] = Main.nchoosek [i][i] = 1
            i += 1
        i = 2
        while i < len(Main.nchoosek):
            for j in range(1, i):
                Main.nchoosek [i][j] = math.fmod((Main.nchoosek [i - 1][j] + Main.nchoosek [i - 1][j - 1]), Main.mod)
            i += 1
        sc = java.util.Scanner(System.in)
        k = sc.nextInt()
        n = sc.nextInt()
        i = 2
        while i <= 2 * k:
            pairs = 0
            if i > k:
                pairs = k - math.trunc(i / float(2))
            else:
                pairs = math.trunc((i - 1) / float(2))
            active = k - 2 * pairs
            if math.fmod(i, 2) == 0:
                active -= 1
            times2 = 1
            total = 0
            for j in range(0, pairs + 1):
                choice = math.fmod(times2 * Main.nchoosek [pairs][j], Main.mod)
                times2 = math.fmod(times2 * 2, Main.mod)
                if active + j - 1 < 0:
                    continue
                total += choice * Main.nchoosek [n + active - 1][active + j - 1]
                if math.fmod(i, 2) == 0:
                    total += choice * Main.nchoosek [n + active - 2][active + j - 1]

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
