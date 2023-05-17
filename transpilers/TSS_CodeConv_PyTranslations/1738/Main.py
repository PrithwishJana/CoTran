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

    check = {}
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        br = BufferedReader(InputStreamReader(System.in))
        buf = None
        input = None
        N = 0
        N = int(br.readLine())
        print(Main.solve(N))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(n):
        a = 0
        b = 0
        if n == 0:
            return 1
        if n == 1:
            return 2
        if math.trunc(n / float(2)) in Main.check.keys():
            a = Main.check[math.trunc(n / float(2))]
        else:
            a = math.fmod(Main.solve(math.trunc(n / float(2))), 1000000007)
            Main.check[math.trunc(n / float(2))] = a
        if math.trunc(n / float(2)) - 1 in Main.check.keys():
            b = Main.check[math.trunc(n / float(2)) - 1]
        else:
            b = math.fmod(Main.solve(math.trunc(n / float(2)) - 1), 1000000007)
            Main.check[math.trunc(n / float(2)) - 1] = b
        if math.fmod(n, 2) == 1:
            return math.fmod((2 * a + b), 1000000007)
        else:
            return math.fmod((2 * b + a), 1000000007)
