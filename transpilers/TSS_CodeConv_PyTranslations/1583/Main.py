﻿//====================================================================================================
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

    Main._sc = java.util.Scanner(System.in)
    line = None
    Main.MOD = 100000007
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve(len, loop):
        ret = 0
        dp = [0 for _ in range(len + 1)]
        dp [0] = 1
        for i in range(1, len + 1):
            j = 1
            while j <= min(loop, i):
                dp [i] += dp [i - j]
                j += 1
            dp [i] = math.fmod(dp [i], Main.MOD)
            if math.fmod((len - i), loop) == 0:
                ret += dp [i]
                ret = math.fmod(ret, Main.MOD)
        return ret
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def solve():
        ans = 1
        prev = 0
        i = 1
        while i < len(Main.line):
            if Main.line[i] != Main.line[i - 1]:
                ans *= Main.solve(i - prev, Main.loop(Main.line[prev]))
                ans = math.fmod(ans, Main.MOD)
                prev = i
            i += 1
        ans *= Main.solve(len(Main.line) - prev, Main.loop(Main.line[prev]))
        ans = math.fmod(ans, Main.MOD)
        return int(ans)
    @staticmethod
    def loop(c):
        return 3 if c == '8' or c == '0' else 5
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
