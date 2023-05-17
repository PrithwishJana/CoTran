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
    def pivotedBinarySearch(arr, n, key):
        pivot = Main.findPivot(arr, 0, n - 1)
        if pivot == - 1:
            return Main.binarySearch(arr, 0, n - 1, key)
        if arr [pivot] == key:
            return pivot
        if arr [0] <= key:
            return Main.binarySearch(arr, 0, pivot - 1, key)
        return Main.binarySearch(arr, pivot + 1, n - 1, key)
    @staticmethod
    def findPivot(arr, low, high):
        if high < low:
            return - 1
        if high == low:
            return low
        mid = math.trunc((low + high) / float(2))
        if mid < high and arr [mid] > arr [mid + 1]:
            return mid
        if mid > low and arr [mid] < arr [mid - 1]:
            return (mid - 1)
        if arr [low] >= arr [mid]:
            return Main.findPivot(arr, low, mid - 1)
        return Main.findPivot(arr, mid + 1, high)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def binarySearch(arr, low, high, key):
        if high < low:
            return - 1
        mid = math.trunc((low + high) / float(2))
        if key == arr [mid]:
            return mid
        if key > arr [mid]:
            return Main.binarySearch(arr, (mid + 1), high, key)
        return Main.binarySearch(arr, low, (mid - 1), key)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
