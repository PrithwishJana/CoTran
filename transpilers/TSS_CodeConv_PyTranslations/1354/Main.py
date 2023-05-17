//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

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
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        main = Main()
        main._solveD()
    def _solveD(self):
        sc = java.util.Scanner(System.in)
        N = sc.nextInt()
        t = [0 for _ in range(N)]
        sum_t = 0
        for i in range(0, N):
            t [i] = sc.nextInt() * 2
            sum_t += t [i]
        v = [0 for _ in range(N)]
        for i in range(0, N):
            v [i] = sc.nextInt() * 2
        tmp_v = 0
        tmp_t = 0
        max_v = [0 for _ in range(sum_t + 1)]
        for i in range(0, N):
            max_v [tmp_t] = v [i] if v [i] < tmp_v else tmp_v
            tmp_v = max_v [tmp_t]
            t_ind = 0
            while t_ind < t [i]:
                tmp_t += 1
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: max_v [++ tmp_t] = v [i] < tmp_v + 1 ? v [i] : tmp_v + 1;
                max_v [ tmp_t] = v [i] if v [i] < tmp_v + 1 else tmp_v + 1
                tmp_v = max_v [tmp_t]
                t_ind += 1
        tmp_v = 0
        for i in range(N - 1, -1, -1):
            max_v [tmp_t] = v [i] if v [i] < tmp_v else tmp_v
            tmp_v = max_v [tmp_t]
            t_ind = 0
            while t_ind < t [i]:
                back_v = v [i] if v [i] < tmp_v + 1 else tmp_v + 1
                tmp_t -= 1
                max_v [tmp_t] = max_v [tmp_t] if max_v [tmp_t] < back_v else back_v
                tmp_v = max_v [tmp_t]
                t_ind += 1

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
