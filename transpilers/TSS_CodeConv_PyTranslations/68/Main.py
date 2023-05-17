//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class Main(Runnable):

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

#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(self, a, c):
        if self.visited [a]:
            if self.color [a] >= 0 and self.color [a] != c:
                self.mujun = True
            return 0
        self.visited [a] = True
        self.color [a] = c
        total = 1
        for b in self.graph [a]:
            total += Main._dfs(b, 1 - c)
        return total
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def run(self):
        scan = Scanner(System.in)
        n = scan.nextInt()
        m = scan.nextInt()
        self.graph = [None for _ in range(n)]
        for i in range(0, n):
            self.graph [i] = []
        for i in range(0, m):
            u = scan.nextInt() - 1
            v = scan.nextInt() - 1
            self.graph [u].append(v)
            self.graph [v].append(u)
        self.visited = [False for _ in range(n)]
        self.color = [0 for _ in range(n)]
        Arrays.fill(self.color, - 1)
        self.one = 0
        self.bipartite = 0
        Main.count = 0
        for i in range(0, n):
            if self.visited [i]:
                continue
            Main.count += 1
            self.mujun = False
            kind = Main._dfs(i, 0)
            if kind == 1:
                self.one += 1
            elif not self.mujun:

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
