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

#JAVA TO PYTHON CONVERTER TASK: There is no Python equivalent to multiple constructors:
#ORIGINAL LINE: Main()
    def __init__(self):
        self._initialize_instance_fields()

        in_ = Scanner(System.in)
        Main._N = in_.nextInt()
        in_.close()
        Main.memo = [None for _ in range(Main._N + 1)]
        i = 0
        while i < len(Main.memo):
            Main.memo [i] = {}
            i += 1
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def calc(self):
        return self.dfs(0, "TTT")
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def isOK(self, last4):
        if "AGC" in last4:
            return False
        for i in range(0, 3):
            vals = last4.toCharArray()
            vals [i] = last4[i + 1]
            vals [i + 1] = last4[i]
            s = str(vals)
            if "AGC" in s:
                return False
        return True
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def dfs(self, current, last3):
        if Main.memo [current].containsKey(last3):
            return int((Main.memo [current].get(last3)))
        if current == Main._N:
            return 1
        result = 0
        for c in self.TOKENS:
            if self.isOK(last3 + c):
                result = math.fmod((result + self.dfs(current + 1, last3[1:len(last3)] + c)), Main.MOD)
        Main.memo [current].put(last3, result)
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        ins = Main()

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
