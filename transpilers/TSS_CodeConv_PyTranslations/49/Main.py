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

    def del_(self, map, y, x):
        map [y][x] = False
        for i in range(0, 4):
            nx = x + self.ofs [i][0]
            ny = y + self.ofs [i][1]
            if 0 <= ny and ny < Main._N and 0 <= nx and nx < Main._N:
                if map [ny][nx]:
                    self.del_(map, ny, nx)
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(self, map):
        c = 0
        y = 0
        while y < Main._N:
            x = 0
            while x < Main._N:
                if map [y][x]:
                    c += 1
                    self.del_(map, y, x)
                x += 1
            y += 1
        return c
    def io(self):
        sc = java.util.Scanner(System.in)
        while sc.hasNext():
            str = [['\0' for _ in range(Main._N)] for _ in range(Main._N)]
            i = 0
            while i < Main._N:
                str [i] = sc.nextLine().toCharArray()
                i += 1
            map = [[False for _ in range(Main._N)] for _ in range(Main._N)]
            y = 0
            while y < Main._N:
                x = 0
                while x < Main._N:
                    map [y][x] = str [y][x] == '1'
                    x += 1
                y += 1
            print(self.solve(map))
            if sc.hasNext():

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
