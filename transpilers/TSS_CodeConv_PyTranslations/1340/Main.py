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

    _N = 0
    _K = 0
    _vec = None
    _ans = 0
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        #JAVA TO PYTHON CONVERTER TASK: Only expression lambdas are converted by Java to Python Converter:
        #    new Thread(null, () ->
        #    {
        #      Scanner sc = new Scanner(System.in)
        #      N = sc.nextInt()
        #      K = sc.nextInt()
        #      ans = 0
        #      vec = new ArrayList [N]
        #      for (int i = 0 ; i < N ; i ++)
        #      {
        #        vec [i] = new ArrayList < > (0)
        #      }
        #      for (int i = 0 ; i < N ; i ++)
        #      {
        #        int a = sc.nextInt() - 1
        #        if (i != 0)
        #        {
        #          vec [a].add(i)
        #        }
        #        else
        #        {
        #          if (a != 0)
        #          {
        #            ans ++
        #          }
        #        }
        #      }
        #      dfs(0, 0)
        #      System.out.println(ans)
        #    }
        #   , "", 1 << 24).start()
        pass
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def _dfs(v, pre):
        hight = 0
        for j, unusedItem in enumerate(Main._vec [v]):
            hight = max(hight, dfs(Main._vec [v].get(j), v))
        if pre != 0 and hight == Main._K - 1:
            hight = 0
            Main._ans += 1
        else:
            hight += 1
        return hight
