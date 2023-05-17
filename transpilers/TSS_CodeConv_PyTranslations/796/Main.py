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
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        (Main())._run()
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private void run() throws java.io.IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _run(self):
        scanner = java.util.Scanner(System.in)
        Main.w = scanner.nextInt()
        Main.h = scanner.nextInt()
        Main.map = [[False for _ in range(Main.w + 2)] for _ in range(Main.h + 2)]
        self.v = [[False for _ in range(Main.w + 2)] for _ in range(Main.h + 2)]
        i = 1
        while i <= Main.h:
            j = 1
            while j <= Main.w:
                Main.map [i][j] = scanner.nextInt() == 1
                j += 1
            i += 1
        print(self._slove(0, 0))
    def _slove(self, y, x):
        self.v [y][x] = True
        res = 0
        for i in range(0, 6):
            ny = y + self.dy [i]
            nx = x + (self.dx1 [i] if math.fmod(y, 2) == 1 else self.dx2 [i])
            if not self._isOK(ny, nx):
                continue
            if Main.map [ny][nx]:
                res += 1
                continue
            if self.v [ny][nx]:
                continue
            res += self._slove(ny, nx)
        return res
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _isOK(self, ny, nx):
        if 0 <= ny and ny <= Main.h + 1 and 0 <= nx and nx <= Main.w + 1:
            return True
        return False
