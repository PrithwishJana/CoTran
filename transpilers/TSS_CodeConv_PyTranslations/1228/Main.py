import math

#JAVA TO PYTHON CONVERTER TASK: Java 'import static' statements are not converted by Java to Python Converter:
#import static Math. *
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

#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def run(self):
        sc = Scanner(System.in)
        h = sc.nextInt()
        w = sc.nextInt()
        if w == 1:
            ret = 1
            for i in range(0, h):
                ret = math.fmod(ret * 2, Main.MOD)
            print(ret)
            return
        cnt = [[0 for _ in range(self.len)] for _ in range(2)]
        cnt [0][0] = 1
        p = 1
        for i in range(0, h + 1):
            fill(cnt [p], 0)
            j = 0
            while j < self.len:
                k = 0
                while k < len(self.es [j]):
                    cnt [p][self.es [j][k]] = math.fmod((cnt [p][self.es [j][k]] + cnt [1 - p][j]), Main.MOD)
                    k += 1
                j += 1
            p = 1 - p
        print(cnt [1 - p][2])
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def debug(self, *os):
        System.err.println(Arrays.deepToString(os))
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        (Main())._run()
