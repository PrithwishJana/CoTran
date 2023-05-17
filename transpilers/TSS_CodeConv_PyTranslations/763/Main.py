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

    g = None
    @staticmethod
    def maxMatching(v, p):
        a = 0
        o = 0
        for w in Main.g [v]:
            if w == p:
                continue
            r = Main.maxMatching(w, v)
            a += math.trunc(r / float(2))
            o += math.fmod(r, 2)
        return 2 * a + min(1, o) + 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sc = MyScanner()
        Main.OUT = PrintWriter(BufferedOutputStream(System.out))
        n = sc.nextInt()
        Main.g = [None for _ in range(n)]
        Arrays.setAll(Main.g, lambda Main.x : [])
        i = 0
        while i < n - 1:
            a = sc.nextInt() - 1
            b = sc.nextInt() - 1
            Main.g [a].append(b)
            Main.g [b].append(a)
            i += 1
        m = math.trunc(Main.maxMatching(0, - 1) / float(2))
        Main.OUT.println("Second" if 2 * m == n else "First")
        Main.OUT.close()
    OUT = None
    class MyScanner:
        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.reader = java.io.BufferedReader(java.io.InputStreamReader(System.in), 1 << 15)
            self.tokenizer = None
            self.br = None
            self.st = None

            self.br = BufferedReader(InputStreamReader(System.in))
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
