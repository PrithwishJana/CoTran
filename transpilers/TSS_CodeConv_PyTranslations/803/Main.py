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
        sc = Scanner(System.in)
        n = sc.nextInt()
        a = [0 for _ in range(n)]
        for i in range(0, n):
            a [i] = sc.nextInt()
        sc.close()
        nodec = True
        for i in range(1, n):
            if a [i] <= a [i - 1]:
                nodec = False
        if nodec:
            print(1)
            return
        m = 500
        l = 1
        r = 210000
        mid = 2
        dec = [0 for _ in range(m)]
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#        out :
        while r - l > 1:
            mid = math.trunc((l + r) / float(2))
            dec = [0 for _ in range(m)]
            Arrays.fill(dec, 1)
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#            nout :
            for i in range(1, n):
                if a [i] <= a [i - 1] and a [i] - 1 < m:
                    if dec [a [i] - 1] < mid:
                        dec [a [i] - 1] += 1
                    else:
                        pos = a [i] - 1
                        while pos > 0:
                            dec [pos - 1] += 1
                            for j in range(pos, m):
                                dec [j] = 1
                            if dec [pos - 1] <= mid:
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#                                continue nout
                            pos -= 1
                        l = mid
#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to Java labels and gotos:
#                        continue out

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
