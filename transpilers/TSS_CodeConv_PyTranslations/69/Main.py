//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

from org.w3c.dom.ls import LSInput
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
        inputStream = System.in
        outputStream = System.out
        in_ = InputReader(inputStream)
        out = java.io.PrintWriter(outputStream)
        solver = TaskA()
        solver.solve(1, in_, out)
        out.close()
    class TaskA:
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def solve(self, testNumber, in_, out):
            n = in_.nextInt()
            m = in_.nextInt()
            k = in_.nextInt()
            c = 1
            s = m - n
            l = k
            r = k
            while s >= r - l + 1:
                s -= r - l + 1
                c += 1
                if l > 1:
                    l -= 1
                if r < n:
                    r += 1
            print(c)
    class InputReader:

        def _initialize_instance_fields(self):
            #instance fields found by Java to Python Converter:
            self.reader = None
            self.tokenizer = None

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: public InputReader(java.io.InputStream stream)
        def __init__(self, stream):
            self._initialize_instance_fields()

            self.reader = java.io.BufferedReader(java.io.InputStreamReader(stream), 32768)
            self.tokenizer = None
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
        def next(self):
            while self.tokenizer is None or not self.tokenizer.hasMoreTokens():
                try:

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
