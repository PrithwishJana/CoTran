//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

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

    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Scanner stdin = new Scanner(System.in);
        stdin = Scanner(System.in)
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int d = stdin.nextInt();
        d = stdin.nextInt()
        dx = [0, 1, 0, - 1]
        dy = [- 1, 0, 1, 0]
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        for t in range(0, d):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int n = stdin.nextInt();
            n = stdin.nextInt()
            map = [['\0' for _ in range(n)] for _ in range(n)]
            for array in map:
                Arrays.fill(array, ' ')
            x = 0
            y = n
            dir = UP
            move = Main.getMoveDistance(n)
            for i in range(0, n):
                j = 0
                while j < move [i]:
                    x += dx [dir]
                    y += dy [dir]
                    map [y][x] = '#'
                    j += 1
                dir = math.fmod((dir + 1), 4)
            for array in map:
                print(str(array))
            if t < d - 1:
                print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: static int [] getMoveDistance(final int n)
    def getMoveDistance(n):
        if n == 1:
            ans = [1]
            return ans
        else:

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
