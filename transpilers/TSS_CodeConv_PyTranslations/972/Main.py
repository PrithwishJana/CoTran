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

    Main.INF = 0x3f3f3f3f
    LNF = 0x3f3f3f3f3f3f3f3f
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        Main.initReader()
        a = Main.nextLong()
        b = Main.nextLong()
        c = Main.nextLong()
        d = Main.nextLong()
        an = [a, b, c]
        Arrays.sort(an)
        ans = 0
        if an [1] - an [0] < d:
            ans += (d - an [1] + an [0])
        if an [2] - an [1] < d:
            ans += (d - an [2] + an [1])
        Main.pw.println(ans)
        Main.pw.close()
    reader = None
    tokenizer = None
    pw = None
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void initReader() throws IOException
    def initReader():
        Main.reader = BufferedReader(InputStreamReader(System.in))
        Main.tokenizer = StringTokenizer("")
        Main.pw = PrintWriter(BufferedWriter(OutputStreamWriter(System.out)))
    @staticmethod
    def hasNext():
        try:
            while not Main.tokenizer.hasMoreTokens():
                Main.tokenizer = StringTokenizer(Main.reader.readLine())
        except Exception as e:
            return False
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static String next() throws IOException
    def next():
        while not Main.tokenizer.hasMoreTokens():
            Main.tokenizer = StringTokenizer(Main.reader.readLine())

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
