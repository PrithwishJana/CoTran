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

    scanner = Scanner(System.in)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        n = Main.scanner.nextInt()
        a = [0 for _ in range(n + 1)]
        b = [0 for _ in range(n + 1)]
        num = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            a [i] = Main.scanner.nextInt()
        for i in range(1, n + 1):
            b [i] = Main.scanner.nextInt()
        for i in range(1, n + 1):
            num [b [i]] += 1
        ss = ""
        ans = 0
        st = [False for _ in range(n + 1)]
        for i in range(1, n + 1):
            if a [i] == 1:
                st [i] = True
                sb = StringBuilder()
                x = b [i]
                sss = StringBuilder()
                sss.append(i)
                sb.append(" " + sss.reverse())
                s = 1
                while (not st [x]) and num [x] == 1 and x != 0 and a [x] != 1:
                    sss = StringBuilder()
                    sss.append(x)
                    sb.append(" " + sss.reverse())
                    st [x] = True
                    x = b [x]
                    s += 1
                if s > ans:
                    ans = s
                    ss = str(sb.reverse())
        print(ans)
        print(ss)
