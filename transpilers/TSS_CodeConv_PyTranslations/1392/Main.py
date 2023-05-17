//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class Graph:

    def _initialize_instance_fields(self):
        #instance fields found by Java to Python Converter:
        self._V = 0
        self._adj = None
        self._totalVertex = 0
        self._adjList = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public Graph()
    def __init__(self):
        self._initialize_instance_fields()

        self._totalVertex = 0
    def loadAdjList(self):
        in_ = java.util.Scanner(System.in)
        self._totalVertex = in_.nextInt()
        self._adjList = java.util.LinkedList()
        i = 0
        while i < self._totalVertex:
            tmp = java.util.LinkedList()
            idx1 = in_.nextInt() - 1
            degree = in_.nextInt()
            for j in range(0, degree):
                idx2 = in_.nextInt() - 1
                tmp.add(idx2)
            self._adjList.add(tmp)
            i += 1
        in_.close()
    def printAdjMatrix(self):
        adjMatrix = [[0 for _ in range(self._totalVertex)] for _ in range(self._totalVertex)]
        i = 0
        while i < self._totalVertex:
            vertexes = self._adjList.get(i)
            j = 0
            while j < self._totalVertex:
                if vertexes.contains(j):
                    adjMatrix [i][j] = 1
                    print("1", end = '')
                else:
                    adjMatrix [i][j] = 0
                    print("0", end = '')
                if j != self._totalVertex - 1:
                    print(" ", end = '')
                j += 1
            print()
            i += 1
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

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
