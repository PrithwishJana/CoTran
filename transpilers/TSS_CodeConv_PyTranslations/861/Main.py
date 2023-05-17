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

#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: void main() throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(self):
        N = Main._sc.nextInt()
        M = Main._sc.nextInt()
        w = [0 for _ in range(N)]
        for i in range(0, M):
            a = Main._sc.nextInt()
            L = Main._sc.nextInt()
            for j in range(0, L):
                w [math.fmod((a + j), N)] = 1
        t = [0 for _ in range(N + 1)]
        s = 0
        f = 0
        s0 = 0
        i = 0
        for i in range(0, N):
            if f == 0 and w [i] == 1:
                s = i
                f = 1
            elif f == 1 and w [i] == 0:
                f = 0
                if s == 0:
                    s0 = i
                else:
                    t [i - s] += 1
        if f == 1:
            t [i - s + s0] += 1
        elif s0 != 0:
            t [s0] += 1
        for i in range(N, 0, -1):
            if t [i] > 0:
                self.result.println(str(i) + " " + str(t [i]))

    class OutputStreamAnonymousInnerClass(OutputStream):
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def write(self, b):
            pass
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        (Main()).main()
